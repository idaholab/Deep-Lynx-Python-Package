# coding: utf-8

"""
    DeepLynx

    The construction of megaprojects has consistently demonstrated challenges for project managers in regard to meeting cost, schedule, and performance requirements. Megaproject construction challenges are common place within megaprojects with many active projects in the United States failing to meet cost and schedule efforts by significant margins. Currently, engineering teams operate in siloed tools and disparate teams where connections across design, procurement, and construction systems are translated manually or over brittle point-to-point integrations. The manual nature of data exchange increases the risk of silent errors in the reactor design, with each silent error cascading across the design. These cascading errors lead to uncontrollable risk during construction, resulting in significant delays and cost overruns. DeepLynx allows for an integrated platform during design and operations of mega projects. The DeepLynx Core API delivers a few main features. 1. Provides a set of methods and endpoints for manipulating data in an object oriented database. This allows us to store complex datatypes as records and then to compile them into actual, modifiable objects at run-time. Users can store taxonomies or ontologies in a readable format. 2. Provides methods for storing and retrieving data in a graph database. This data is structured and validated against the aformentioned object oriented database before storage.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Node(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'container_id': 'str',
        'metatype_id': 'str',
        'metatype': 'NodeMetatypeBody',
        'metatype_name': 'str',
        'data_source_id': 'str',
        'import_data_id': 'str',
        'data_staging_id': 'float',
        'type_mapping_transformation_id': 'str',
        'original_data_id': 'str',
        'properties': 'object',
        'metadata': 'object',
        'created_at': 'str',
        'modified_at': 'str',
        'deleted_at': 'str',
        'created_by': 'str',
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'container_id': 'container_id',
        'metatype_id': 'metatype_id',
        'metatype': 'metatype',
        'metatype_name': 'metatype_name',
        'data_source_id': 'data_source_id',
        'import_data_id': 'import_data_id',
        'data_staging_id': 'data_staging_id',
        'type_mapping_transformation_id': 'type_mapping_transformation_id',
        'original_data_id': 'original_data_id',
        'properties': 'properties',
        'metadata': 'metadata',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'deleted_at': 'deleted_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, container_id=None, metatype_id=None, metatype=None, metatype_name=None, data_source_id=None, import_data_id=None, data_staging_id=None, type_mapping_transformation_id=None, original_data_id=None, properties=None, metadata=None, created_at=None, modified_at=None, deleted_at=None, created_by=None, modified_by=None):  # noqa: E501
        """Node - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._container_id = None
        self._metatype_id = None
        self._metatype = None
        self._metatype_name = None
        self._data_source_id = None
        self._import_data_id = None
        self._data_staging_id = None
        self._type_mapping_transformation_id = None
        self._original_data_id = None
        self._properties = None
        self._metadata = None
        self._created_at = None
        self._modified_at = None
        self._deleted_at = None
        self._created_by = None
        self._modified_by = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if container_id is not None:
            self.container_id = container_id
        if metatype_id is not None:
            self.metatype_id = metatype_id
        if metatype is not None:
            self.metatype = metatype
        if metatype_name is not None:
            self.metatype_name = metatype_name
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if import_data_id is not None:
            self.import_data_id = import_data_id
        if data_staging_id is not None:
            self.data_staging_id = data_staging_id
        if type_mapping_transformation_id is not None:
            self.type_mapping_transformation_id = type_mapping_transformation_id
        if original_data_id is not None:
            self.original_data_id = original_data_id
        if properties is not None:
            self.properties = properties
        if metadata is not None:
            self.metadata = metadata
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        """Gets the id of this Node.  # noqa: E501


        :return: The id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.


        :param id: The id of this Node.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def container_id(self):
        """Gets the container_id of this Node.  # noqa: E501


        :return: The container_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this Node.


        :param container_id: The container_id of this Node.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def metatype_id(self):
        """Gets the metatype_id of this Node.  # noqa: E501


        :return: The metatype_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._metatype_id

    @metatype_id.setter
    def metatype_id(self, metatype_id):
        """Sets the metatype_id of this Node.


        :param metatype_id: The metatype_id of this Node.  # noqa: E501
        :type: str
        """

        self._metatype_id = metatype_id

    @property
    def metatype(self):
        """Gets the metatype of this Node.  # noqa: E501


        :return: The metatype of this Node.  # noqa: E501
        :rtype: NodeMetatypeBody
        """
        return self._metatype

    @metatype.setter
    def metatype(self, metatype):
        """Sets the metatype of this Node.


        :param metatype: The metatype of this Node.  # noqa: E501
        :type: NodeMetatypeBody
        """

        self._metatype = metatype

    @property
    def metatype_name(self):
        """Gets the metatype_name of this Node.  # noqa: E501


        :return: The metatype_name of this Node.  # noqa: E501
        :rtype: str
        """
        return self._metatype_name

    @metatype_name.setter
    def metatype_name(self, metatype_name):
        """Sets the metatype_name of this Node.


        :param metatype_name: The metatype_name of this Node.  # noqa: E501
        :type: str
        """

        self._metatype_name = metatype_name

    @property
    def data_source_id(self):
        """Gets the data_source_id of this Node.  # noqa: E501


        :return: The data_source_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this Node.


        :param data_source_id: The data_source_id of this Node.  # noqa: E501
        :type: str
        """

        self._data_source_id = data_source_id

    @property
    def import_data_id(self):
        """Gets the import_data_id of this Node.  # noqa: E501


        :return: The import_data_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._import_data_id

    @import_data_id.setter
    def import_data_id(self, import_data_id):
        """Sets the import_data_id of this Node.


        :param import_data_id: The import_data_id of this Node.  # noqa: E501
        :type: str
        """

        self._import_data_id = import_data_id

    @property
    def data_staging_id(self):
        """Gets the data_staging_id of this Node.  # noqa: E501


        :return: The data_staging_id of this Node.  # noqa: E501
        :rtype: float
        """
        return self._data_staging_id

    @data_staging_id.setter
    def data_staging_id(self, data_staging_id):
        """Sets the data_staging_id of this Node.


        :param data_staging_id: The data_staging_id of this Node.  # noqa: E501
        :type: float
        """

        self._data_staging_id = data_staging_id

    @property
    def type_mapping_transformation_id(self):
        """Gets the type_mapping_transformation_id of this Node.  # noqa: E501


        :return: The type_mapping_transformation_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._type_mapping_transformation_id

    @type_mapping_transformation_id.setter
    def type_mapping_transformation_id(self, type_mapping_transformation_id):
        """Sets the type_mapping_transformation_id of this Node.


        :param type_mapping_transformation_id: The type_mapping_transformation_id of this Node.  # noqa: E501
        :type: str
        """

        self._type_mapping_transformation_id = type_mapping_transformation_id

    @property
    def original_data_id(self):
        """Gets the original_data_id of this Node.  # noqa: E501


        :return: The original_data_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._original_data_id

    @original_data_id.setter
    def original_data_id(self, original_data_id):
        """Sets the original_data_id of this Node.


        :param original_data_id: The original_data_id of this Node.  # noqa: E501
        :type: str
        """

        self._original_data_id = original_data_id

    @property
    def properties(self):
        """Gets the properties of this Node.  # noqa: E501


        :return: The properties of this Node.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Node.


        :param properties: The properties of this Node.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def metadata(self):
        """Gets the metadata of this Node.  # noqa: E501


        :return: The metadata of this Node.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Node.


        :param metadata: The metadata of this Node.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def created_at(self):
        """Gets the created_at of this Node.  # noqa: E501


        :return: The created_at of this Node.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Node.


        :param created_at: The created_at of this Node.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Node.  # noqa: E501


        :return: The modified_at of this Node.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Node.


        :param modified_at: The modified_at of this Node.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Node.  # noqa: E501


        :return: The deleted_at of this Node.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Node.


        :param deleted_at: The deleted_at of this Node.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def created_by(self):
        """Gets the created_by of this Node.  # noqa: E501


        :return: The created_by of this Node.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Node.


        :param created_by: The created_by of this Node.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Node.  # noqa: E501


        :return: The modified_by of this Node.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Node.


        :param modified_by: The modified_by of this Node.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Node, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
