# Copyright 2021, Battelle Energy Alliance, LLC

import logging
import requests
from requests_toolbelt import MultipartEncoder
from typing import Dict, Any


class DeepLynxService:
    """Interacts with and makes calls to Deep Lynx.

    Deep Lynx Service requires parameters defining the connection to Deep Lynx.
    It contains the API suite for interacting with the various elements of
    Deep Lynx.

    Args:
        deep_lynx_url: Base url to reach Deep Lynx.
        container_name: Name of the Deep Lynx container.
        data_source_name: Desired name to register for this application.
        token: The authentication token (optional).
        origin: The origin for CORS (optional).
        init: Indicates whether a connection with Deep Lynx should be made
            and the Container and Data Source verified (default of False).
    """
    def __init__(self,
                 deep_lynx_url: str,
                 container_name: str,
                 data_source_name: str,
                 token: str = None,
                 origin: str = None,
                 init: bool = False):
        """Initializes a Deep Lynx Service object."""
        self.deep_lynx_url: str = deep_lynx_url
        self.container_name: str = container_name
        self.data_source_name: str = data_source_name

        self.container_id: str = None
        self.data_source_id: str = None

        self.headers: Dict[str, str] = None

        # initialize API header
        self.set_headers(token, origin)

        # setup logger that allows the package user to control it through the standard logging API
        logging.getLogger('deep-lynx').addHandler(logging.NullHandler())

        if init:
            self.init()

    # HELPER AND LOGIC FUNCTIONS

    # public method so that a user can update the token and origin values
    def set_headers(self, token: str = None, origin: str = None) -> None:
        """Sets the API request headers to be used with Deep Lynx.

        Args:
            token: The authentication token (optional).
            origin: The origin for CORS (optional).

        Returns:
            None
        """
        # if origin is not provided, default CORS to wildcard origin
        if origin is None:
            origin = '*'

        if token is not None:
            self.headers = {'Access-Control-Allow-Origin': origin, 'Authorization': 'Bearer ' + token}
        else:
            self.headers = {'Access-Control-Allow-Origin': origin}

    def init(self) -> None:
        """Makes initial contact with Deep Lynx.

        Retrieves container and datasource IDs.

        Args:
            None

        Returns:
            None
        """
        if self.check_container():
            verified = self.check_data_source()
            if not verified:
                logging.error('Unable to find or register the provided data source name')
            else:
                logging.info(
                    f'Successful connection to Deep Lynx container {self.container_id} and data source {self.data_source_id}'
                )
        else:
            logging.error('Deep Lynx container does not exist or Deep Lynx cannot be reached')

    def check_container(self, offset: int = 0, limit: int = 100) -> bool:
        """Ensures that the provided container exists in Deep Lynx.

        If a container does not exist with the provided name, a value of `False`
        is returned. This method does NOT attempt to create the missing container.

        Args:
            offset: The number of results to skip before return (optional).
            limit: The number of results to return in a single request (optional).

        Returns:
            Bool indicating whether container was found.
        """
        params = {'offset': offset, 'limit': limit}

        try:
            # implement error handling for the first call to Deep Lynx
            # in case the instance is not running or reachable
            resp = requests.get(self.deep_lynx_url + '/containers', params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            return False

        for container in resp.json()['value']:
            name = container['name']
            if name == self.container_name:
                self.container_id = container['id']
                return True
        logging.warning(f'Container with name {self.container_name} does not exist')
        return False

    def check_data_source(self, adapter_type: str = 'standard', config: Dict[Any, Any] = {}) -> bool:
        """Determines if the data source exists. Creates it if it does not exist.

        Args:
            adapter_type: string with value `standard` (default) or `http`

        Returns:
            Bool indicating whether data source was found/created.
        """
        data_sources = self.list_data_sources(self.container_id)

        if len(data_sources['value']) > 0:
            for datasource in data_sources['value']:
                name = datasource['name']
                if name == self.data_source_name:
                    self.data_source_id = datasource['id']
                    return True

        # matching data source has not been found, attempt to create a new one
        body = {'adapter_type': adapter_type, 'active': True, 'name': self.data_source_name, 'config': config}
        new_data_source = self.create_data_source(self.container_id, payload=body)
        if new_data_source['isError']:
            return False
        else:
            self.data_source_id = new_data_source['value']['id']
            logging.info(f'New datasource created with name {self.data_source_name}')
            return True

    def get_latest_import_time(self) -> Any:
        """Retrieves the latest import time for this data source.

        Args:
            None

        Returns:
            Timestamp of latest import or False on an error or no imports.
        """
        imports = self.list_imports_for_data_source(self.container_id, self.data_source_id)
        if imports['isError']:
            return False
        else:
            if len(imports['value']) > 0:
                for data_import in imports['value']:
                    created_at = data_import['created_at']
                    return created_at
            return False

    # CONTAINERS

    def health(self):
        """Deep Lynx health endpoint."""
        return self.__get('/health')

    def create_container(self, payload: Dict[Any, Any]):
        """Creates a Deep Lynx container."""
        return self.__post('/containers', payload)

    def retrieve_container(self, container_id: str):
        """Retrieves a certain container."""
        return self.__get(f'/containers/{container_id}')

    def list_containers(self, params: Dict[str, Any] = {}):
        """Lists all containers."""
        return self.__get('/containers', params)

    def update_container(self, container_id: str, payload: Dict[Any, Any]):
        """Updates a certain container."""
        return self.__put(f'/containers/{container_id}', payload)

    def batch_update_containers(self, payload: Dict[Any, Any]):
        """Updates one or more Deep Lynx containers."""
        # convert payload to list if necessary
        if type(payload) is not list:
            payload = [payload]
        return self.__put('/containers', payload)

    def archive_container(self, container_id: str):
        """Archives a certain container."""
        return self.__delete(f'/containers/{container_id}')

    def set_container_active(self, container_id: str):
        """Sets a certain container active (unarchives it)."""
        return self.__post(f'/containers/{container_id}/active')

    def delete_container(self, container_id: str, params: Dict[str, Any] = {'permanent': 'true'}):
        """Permanently deletes a certain container."""
        return self.__delete(f'/containers/{container_id}', params)

    def import_container(self, form_upload: Dict[str, str]):
        """Creates a container from an ontology file.
        
        One of the following must be provided: A path to a local file
        or a URL path to the ontology file.

        Args:
            form_upload: Dict that must contain - 
                name: The name of the container to be created
                description: A description for the container (optional)
                url_path: A path to the url of the raw `.owl` document OR
                file_path: A path to local file
        """
        if form_upload['file_path']:
            multipart_data = MultipartEncoder(
                fields={
                    'name': form_upload['name'],
                    'description': form_upload['description'],
                    'file': (form_upload['file_path'], open(form_upload['file_path'], 'rb'), 'multipart/form-data'),
                    'data_versioning_enabled': form_upload['data_versioning_enabled']
                })
        else:
            multipart_data = MultipartEncoder(
                fields={
                    'name': form_upload['name'],
                    'description': form_upload['description'],
                    'path': form_upload['url_path'],
                    'data_versioning_enabled': form_upload['data_versioning_enabled']
                })

        return self.__post('/containers/import', data=multipart_data)

    def update_import(self, container_id: str, form_upload: Dict[str, str]):
        """Updates a container from an ontology file.
        
        One of the following must be provided: A path to a local file
        or a URL path to the ontology file.

        Args:
            form_upload: Dict that must contain - 
                name: The name of the container to be created
                description: A description for the container (optional)
                url_path: A path to the url of the raw `.owl` document OR
                file_path: A path to local file
        """
        if form_upload['file_path']:
            multipart_data = MultipartEncoder(
                fields={
                    'name': form_upload['name'],
                    'description': form_upload['description'],
                    'file': (form_upload['file_path'], open(form_upload['file_path'], 'rb'), 'multipart/form-data')
                })
        else:
            multipart_data = MultipartEncoder(fields={
                'name': form_upload['name'],
                'description': form_upload['description'],
                'path': form_upload['url_path']
            })
        return self.__put(f'/containers/import/{container_id}', data=multipart_data)

    def repair_container_permissions(self, container_id: str):
        """Repairs the permissions of a container."""
        return self.__post(f'/containers/{container_id}/permissions')

    # DATA SOURCES

    def create_data_source(self, container_id: str, payload: Dict[Any, Any]):
        """Creates a data source."""
        return self.__post(f'/containers/{container_id}/import/datasources', payload)

    def create_manual_import(self, container_id: str, data_source_id: str, payload: Any):
        """Sends a JSON payload to Deep Lynx for import."""
        # convert payload to list if necessary
        if type(payload) is not list:
            payload = [payload]

        return self.__post(f'/containers/{container_id}/import/datasources/{data_source_id}/imports', payload)

    def list_data_sources(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all registered data sources for some container."""
        return self.__get(f'/containers/{container_id}/import/datasources', params)

    def retrieve_data_source(self, container_id: str, data_source_id: str):
        """Retrieves a certain data source."""
        return self.__get(f'/containers/{container_id}/import/datasources/{data_source_id}')

    def list_imports_for_data_source(self, container_id: str, data_source_id: str, params: Dict[str, Any] = {}):
        """Lists all imports for a data source."""
        return self.__get(f'/containers/{container_id}/import/datasources/{data_source_id}/imports', params)

    def count_unmapped_data(self, container_id: str):
        """Returns a count of all unmapped data records for a container."""
        return self.__get(f'/containers/{container_id}/import/datasources')

    def download_file(self, container_id: str, file_id: str):
        """Downloads a file."""
        return self.__get(f'/containers/{container_id}/files/{file_id}/download')

    def retrieve_file(self, container_id: str, file_id: str):
        """Retrieves a file."""
        return self.__get(f'/containers/{container_id}/files/{file_id}')

    def upload_file(self, container_id: str, data_source_id: str, file_paths: list()):
        """Uploads a file.
        
        Args:
            file_paths: An array of strings with locations to each file
            to be uploaded.
        """
        multipart_data = MultipartEncoder(fields={fname: (fname, open(fname, 'rb')) for fname in file_paths})
        return self.__post(f'/containers/{container_id}/import/datasources/{data_source_id}/files', data=multipart_data)

    def update_datasource_configuration(self, container_id: str, data_source_id: str, payload: Dict[Any, Any]):
        """Updates a datasource configuration."""
        return self.__put(f'/containers/{container_id}/import/datasources/{data_source_id}', payload)

    def set_data_source_active(self, container_id: str, data_source_id: str):
        """Sets a data source's active flag to true."""
        return self.__post(f'/containers/{container_id}/import/datasources/{data_source_id}/active')

    def set_data_source_inactive(self, container_id: str, data_source_id: str):
        """Sets a data source's active flag to false."""
        return self.__delete(f'/containers/{container_id}/import/datasources/{data_source_id}/active')

    def delete_data_source(self, container_id: str, data_source_id: str, params: Dict[str, Any] = {}):
        """Permanently deletes a data source."""
        return self.__delete(f'/containers/{container_id}/import/datasources/{data_source_id}', params)

    # DATA QUERY

    def query(self, container_id: str, payload: Any):
        """Queries the Deep Lynx data using GraphQL."""
        # Endpoint handles both graph and file queries
        return self.__post_plain(f'/containers/{container_id}/query', payload)

    # GRAPH

    def create_update_nodes(self, container_id: str, payload: Dict[Any, Any]):
        """Creates or updates nodes.
        
        Return: A boolean indicating success.
        """
        return self.__post(f'/containers/{container_id}/graphs/nodes', payload)

    def retrieve_node(self, container_id: str, node_id: str):
        """Retrieves a node."""
        return self.__get(f'/containers/{container_id}/graphs/nodes/{node_id}')

    def list_nodes(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all nodes."""
        return self.__get(f'/containers/{container_id}/graphs/nodes', params)

    def list_nodes_by_metatype_id(self, container_id: str, metatype_id: str, params: Dict[str, Any] = {}):
        """Lists all nodes by common metatype ID."""
        return self.__get(f'/containers/{container_id}/graphs/nodes/metatype/{metatype_id}', params)

    def archive_node(self, container_id: str, node_id: str):
        """Archives a node."""
        return self.__delete(f'/containers/{container_id}/graphs/nodes/{node_id}')

    def create_update_edges(self, container_id: str, payload: Dict[Any, Any]):
        """Creates or updates edges."""
        return self.__post(f'/containers/{container_id}/graphs/edges', payload)

    def retrieve_edge(self, container_id: str, edge_id: str):
        """Retrieves an edge."""
        return self.__get(f'/containers/{container_id}/graphs/edges/{edge_id}')

    def list_edges(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all edges."""
        return self.__get(f'/containers/{container_id}/graphs/edges', params)

    def archive_edge(self, container_id: str, edge_id: str):
        """Archives a edge."""
        return self.__delete(f'/containers/{container_id}/graphs/edges/{edge_id}')

    # IMPORTS

    def list_import_data(self, container_id: str, import_id: str, params: Dict[str, Any] = {}):
        """Lists the data from a Deep Lynx import."""
        return self.__get(f'/containers/{container_id}/import/imports/{import_id}/data', params)

    def retrieve_import_data(self, container_id: str, import_id: str, data_id: str):
        """Retrieves the data for a certain import."""
        return self.__get(f'/containers/{container_id}/import/imports/{import_id}/data/{data_id}')

    def delete_import_data(self, container_id: str, import_id: str, data_id: str):
        """Deletes the data for a certain import."""
        return self.__delete(f'/containers/{container_id}/import/imports/{import_id}/data/{data_id}')

    def delete_import(self, container_id: str, import_id: str):
        """Deletes an import."""
        return self.__delete(f'/containers/{container_id}/import/imports/{import_id}')

    # EXPORTS

    def create_data_export(self, container_id: str, payload: Dict[Any, Any]):
        """Creates a data export."""
        return self.__post(f'/containers/{container_id}/data/export', payload)

    def retrieve_data_export(self, container_id: str, export_id: str):
        """Retrieves a data export."""
        return self.__get(f'/containers/{container_id}/data/export/{export_id}')

    def start_data_export(self, container_id: str, export_id: str):
        """Starts a data export."""
        return self.__post(f'/containers/{container_id}/data/export/{export_id}')

    def stop_data_export(self, container_id: str, export_id: str, payload: Dict[Any, Any]):
        """Stops a data export."""
        return self.__put(f'/containers/{container_id}/data/export/{export_id}', payload)

    def delete_data_export(self, container_id: str, export_id: str):
        """Deletes a data export."""
        return self.__delete(f'/containers/{container_id}/data/export/{export_id}')

    # EVENTS

    def create_registered_event(self, payload: Dict[Any, Any]):
        """Registers for an event on some container or data source."""
        return self.__post('/events', payload)

    def list_registered_events(self, params: Dict[str, Any] = {}):
        """Lists all registered events."""
        return self.__get('/events', params)

    def retrieve_registered_event(self, event_id: str):
        """Retrieves a certain registered event."""
        return self.__get(f'/events/{event_id}')

    def update_registered_event(self, event_id: str, payload: Dict[Any, Any], active: bool = True):
        """Updates a registered event."""
        return self.__put(f'/events/{event_id}', payload, params={'active': active})

    def delete_registered_event(self, event_id: str):
        """Deletes a registered event."""
        return self.__delete(f'/events/{event_id}')

    # DATA TYPE MAPPINGS

    def create_type_mapping_transformation(self, container_id: str, data_source_id: str, mapping_id: str,
                                           payload: Dict[Any, Any]):
        """Creates a type mapping transformation."""
        return self.__post(
            f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations',
            payload)

    def list_type_mappings(self, container_id: str, data_source_id: str, params: Dict[str, Any] = {}):
        """Lists all type mappings."""
        return self.__get(f'/containers/{container_id}/import/datasources/{data_source_id}/mappings', params)

    def retrieve_type_mapping(self, container_id: str, data_source_id: str, mapping_id: str):
        """Retrieves a certain registered event."""
        return self.__get(f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}')

    def list_type_mapping_transformations(self,
                                          container_id: str,
                                          data_source_id: str,
                                          mapping_id: str,
                                          params: Dict[str, Any] = {}):
        """Lists all transformations for a type mapping."""
        return self.__get(
            f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations',
            params)

    def update_type_mapping_transformations(self, container_id: str, data_source_id: str, mapping_id: str,
                                            transformation_id: str, payload: Dict[Any, Any]):
        """Updates a transformation for a type mapping."""
        return self.__put(
            f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations/{transformation_id}',
            payload)

    def delete_type_mapping_transformations(self, container_id: str, data_source_id: str, mapping_id: str,
                                            transformation_id: str):
        """Deletes a transformation."""
        return self.__delete(
            f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations/{transformation_id}'
        )

    def delete_type_mapping(self, container_id: str, data_source_id: str, mapping_id: str):
        """Deletes a type mapping."""
        return self.__delete(f'/containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}')

    # USERS

    def generate_user_keypair(self, user_id: str, payload: Dict[Any, Any]):
        """Creates a keypair for a user."""
        return self.__post(f'/users/{user_id}/keys', payload)

    def assign_role(self, container_id: str, payload: Dict[Any, Any]):
        """Assigns a role to a user."""
        return self.__post(f'/containers/{container_id}/users/roles', payload)

    def reset_password(self, payload: Dict[Any, Any]):
        """Request a password reset for a user."""
        return self.__post('/users/reset-password', payload)

    def invite_user_to_container(self, container_id: str, payload: Dict[Any, Any]):
        """Invites a user to a container."""
        return self.__post(f'/containers/{container_id}/users/invite', payload)

    def retrieve_user(self, container_id: str, user_id: str):
        """Retrieves a user."""
        return self.__get(f'/containers/{container_id}/users/{user_id}')

    def list_users(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all users."""
        return self.__get(f'/containers/{container_id}/users', params)

    def list_user_roles(self, container_id: str, user_id: str, params: Dict[str, Any] = {}):
        """Lists roles for a user."""
        return self.__get(f'/containers/{container_id}/users/{user_id}/roles', params)

    def validate_email(self, params: Dict[str, Any] = {}):
        """Validates the email for a user.

        Args:
            params: Dict that should contain `id` and `token`.
        """
        return self.__get('/users/validate', params)

    def request_password_reset(self, params: Dict[str, Any] = {}):
        """Requests a password reset for a certain email.

        Args:
            params: Dict that should contain `email`.
        """
        return self.__get('/users/reset-password', params)

    def list_container_invited_users(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all invited users for a container."""
        return self.__get(f'/containers/{container_id}/users/invite', params)

    def delete_user_keypair(self, user_id: str, key_id: str):
        """Deletes a keypair for a user."""
        return self.__delete(f'/users/{user_id}/keys/{key_id}')

    # METATYPES

    def create_metatype(self, container_id: str, payload: Dict[Any, Any]):
        """Creates a metatype."""
        return self.__post(f'/containers/{container_id}/metatypes', payload)

    def retrieve_metatype(self, container_id: str, metatype_id: str):
        """Retrieves a metatype."""
        return self.__get(f'/containers/{container_id}/metatypes/{metatype_id}')

    def list_metatypes(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all metatypes.
        
        Args:
            params: Dict that may contain `limit`, `offset`, and `name`.
        """
        return self.__get(f'/containers/{container_id}/metatypes', params)

    def update_metatype(self, container_id: str, metatype_id: str, payload: Dict[Any, Any]):
        """Updates a metatype."""
        return self.__put(f'/containers/{container_id}/metatypes/{metatype_id}', payload)

    def archive_metatype(self, container_id: str, metatype_id: str):
        """Archives a metatype."""
        return self.__delete(f'/containers/{container_id}/metatypes/{metatype_id}')

    # METATYPE KEYS

    def create_metatype_key(self, container_id: str, metatype_id: str, payload: Dict[Any, Any]):
        """Creates a metatype key."""
        return self.__post(f'/containers/{container_id}/metatypes/{metatype_id}/keys', payload)

    def retrieve_metatype_key(self, container_id: str, metatype_id: str, key_id: str):
        """Retrieves a metatype key."""
        return self.__get(f'/containers/{container_id}/metatypes/{metatype_id}/keys/{key_id}')

    def list_metatype_keys(self, container_id: str, metatype_id: str, params: Dict[str, Any] = {}):
        """Lists all keys for a metatype.
        
        Args:
            params: Dict that may contain `limit` and `offset`.
        """
        return self.__get(f'/containers/{container_id}/metatypes/{metatype_id}/keys', params)

    def update_metatype_key(self, container_id: str, metatype_id: str, key_id: str, payload: Dict[Any, Any]):
        """Updates a metatype key."""
        return self.__put(f'/containers/{container_id}/metatypes/{metatype_id}/keys/{key_id}', payload)

    def archive_metatype_key(self, container_id: str, metatype_id: str, key_id: str):
        """Archives a metatype key."""
        return self.__delete(f'/containers/{container_id}/metatypes/{metatype_id}/keys/{key_id}')

    # METATYPE RELATIONSHIPS

    def create_relationship(self, container_id: str, payload: Dict[Any, Any]):
        """Creates a metatype relationship."""
        return self.__post(f'/containers/{container_id}/metatype_relationships', payload)

    def retrieve_relationship(self, container_id: str, relationship_id: str):
        """Retrieves a metatype relationship."""
        return self.__get(f'/containers/{container_id}/metatype_relationships/{relationship_id}')

    def list_relationships(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all metatype relationships.
        
        Args:
            params: Dict that may contain `limit` and `offset`.
        """
        return self.__get(f'/containers/{container_id}/metatype_relationships', params)

    def update_relationship(self, container_id: str, relationship_id: str, payload: Dict[Any, Any]):
        """Updates a metatype relationship."""
        return self.__put(f'/containers/{container_id}/metatype_relationships/{relationship_id}', payload)

    def archive_relationship(self, container_id: str, relationship_id: str):
        """Archives a metatype relationship."""
        return self.__delete(f'/containers/{container_id}/metatype_relationships/{relationship_id}')

    # METATYPE RELATIONSHIP KEYS

    def create_relationship_key(self, container_id: str, relationship_id: str, payload: Dict[Any, Any]):
        """Creates a relationship key."""
        return self.__post(f'/containers/{container_id}/metatype_relationships/{relationship_id}/keys', payload)

    def retrieve_relationship_key(self, container_id: str, relationship_id: str, key_id: str):
        """Retrieves a relationship key."""
        return self.__get(f'/containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id}')

    def list_relationship_keys(self, container_id: str, relationship_id: str, params: Dict[str, Any] = {}):
        """Lists all keys for a relationship.
        
        Args:
            params: Dict that may contain `limit` and `offset`.
        """
        return self.__get(f'/containers/{container_id}/metatype_relationships/{relationship_id}/keys', params)

    def update_relationship_key(self, container_id: str, relationship_id: str, key_id: str, payload: Dict[Any, Any]):
        """Updates a relationship key."""
        return self.__put(f'/containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id}', payload)

    def archive_relationship_key(self, container_id: str, relationship_id: str, key_id: str):
        """Archives a relationship key."""
        return self.__delete(f'/containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id}')

    # METATYPE RELATIONSHIP PAIRS

    def create_relationship_pair(self, container_id: str, payload: Dict[Any, Any]):
        """Creates a metatype relationship pair."""
        return self.__post(f'/containers/{container_id}/metatype_relationship_pairs', payload)

    def retrieve_relationship_pair(self, container_id: str, pair_id: str):
        """Retrieves a metatype relationship pair."""
        return self.__get(f'/containers/{container_id}/metatype_relationship_pairs/{pair_id}')

    def list_relationship_pairs(self, container_id: str, params: Dict[str, Any] = {}):
        """Lists all metatype relationship pairs.
        
        Args:
            params: Dict that may contain `limit` and `offset`.
        """
        return self.__get(f'/containers/{container_id}/metatype_relationship_pairs', params)

    def update_relationship_pair(self, container_id: str, pair_id: str, payload: Dict[Any, Any]):
        """Updates a metatype relationship pair."""
        return self.__put(f'/containers/{container_id}/metatype_relationship_pairs/{pair_id}', payload)

    def archive_relationship_pair(self, container_id: str, pair_id: str):
        """Archives a metatype relationship pair."""
        return self.__delete(f'/containers/{container_id}/metatype_relationship_pairs/{pair_id}')

    # REQUESTS PRIVATE FUNCTIONS

    def __get(self, uri: str, params: Dict[str, Any] = {}):
        try:
            resp = requests.get(self.deep_lynx_url + uri, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            logging.exception(f'Exception: {e}')
            return e

        return self.__requests_handler(resp)

    def __post(self, uri: str, payload: Dict[Any, Any] = {}, params: Dict[str, Any] = {}, data=None):
        try:
            if data is not None:
                # multipart uploads
                self.headers['Content-Type'] = data.content_type
                resp = requests.post(self.deep_lynx_url + uri, params=params, headers=self.headers, data=data)
            else:
                # payload must be sent in json format
                self.headers['Content-Type'] = 'application/json'
                resp = requests.post(self.deep_lynx_url + uri, json=payload, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            logging.exception(f'Exception: {e}')
            return e

        return self.__requests_handler(resp)

    def __post_plain(self, uri: str, payload: Any, params: Dict[str, Any] = {}):
        try:
            self.headers['Content-Type'] = 'text/plain'
            resp = requests.post(self.deep_lynx_url + uri, data=payload, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            logging.exception(f'Exception: {e}')
            return e

        return self.__requests_handler(resp)

    def __put(self, uri: str, payload: Dict[Any, Any] = {}, params: Dict[str, Any] = {}, data=None):
        try:
            if data is not None:
                # multipart uploads
                self.headers['Content-Type'] = data.content_type
                resp = requests.put(self.deep_lynx_url + uri, params=params, headers=self.headers, data=data)
            else:
                # payload must be sent in json format
                self.headers['Content-Type'] = 'application/json'
                resp = requests.put(self.deep_lynx_url + uri, json=payload, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            logging.exception(f'Exception: {e}')
            return e

        return self.__requests_handler(resp)

    def __delete(self, uri: str, params: Dict[str, Any] = {}):
        try:
            resp = requests.delete(self.deep_lynx_url + uri, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:
            logging.exception(f'Exception: {e}')
            return e

        return self.__requests_handler(resp)

    def __requests_handler(self, resp: Any) -> Any:
        if not resp.ok:
            logging.error(f'Error: {resp.text}')

        if ('application/json' in resp.headers.get('content-type')):
            return resp.json()
        else:
            return resp.text
