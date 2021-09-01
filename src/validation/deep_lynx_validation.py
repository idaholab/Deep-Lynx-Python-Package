import os
import json
import datetime
import settings

from deep_lynx.deep_lynx_service import DeepLynxService


class DeepLynxValidator():
    def __init__(self, deep_lynx: DeepLynxService):
        """Initializes a Deep Lynx Validator object."""
        self.deep_lynx: str = deep_lynx

    # PUBLIC FUNCTIONS

    def validate_properties(self, metatype: str, json_data: dict, container_id: str = None):
        """
        Validates the properties and datatype of the json data for a metatype
        Args:
            metatype: name of the metatype
            json_data: a dictionary of the metatype's data
            container_id: a container uuid
        Return:
            error: whether an error occurred e.g. {"isError": false, "error": []}
        """
        error = dict()
        error["isError"] = False
        error["error"] = list()

        # Get the properties
        get_properties_error = self.__get_properties(metatype, container_id)
        get_properties_error = json.loads(get_properties_error)
        if get_properties_error["isError"]:
            error["isError"] = True
            error["error"] = get_properties_error["error"]
        else:
            metatype_properties = get_properties_error["value"]
            is_id_found = False
            for property, value in json_data.items():
                is_property_found = False
                # Check if the property is 'id'
                if property == "id":
                    is_id_found = True
                # Check if the property on the node exists
                for metatype_property, metatype_datatype in metatype_properties.items():
                    if metatype_property == property:
                        is_property_found = True
                        # Check if the correct datatype
                        datatype = self.__identify_datatype(value)
                        if datatype != metatype_datatype:
                            error["error"].append("Wrong datatype for property '{0}'. Change from '{1}' to '{2}".format(
                                property, datatype, metatype_datatype))
                            error["isError"] = True
                if not is_property_found:
                    error["error"].append("Invalid property '{0}' for the metatype '{1}'".format(property, metatype))
                    error["isError"] = True
            if not is_id_found:
                error["error"].append("The 'id' property is required for every metatype")
                error["isError"] = True
        error = json.dumps(error)
        return error

    # PRIVATE FUNCTIONS

    def __get_properties(self, metatype: str, container_id: str = None):
        """
        Return a dictionary with each property name and property datatype for a metatype
        Args:
            metatype: name of the metatype
            container_id: a container uuid
        """
        error = dict()
        error["isError"] = False
        error["error"] = list()
        error["value"] = None

        # Determine the container id
        params = {"name": metatype}
        if not container_id:
            container = self.deep_lynx.container_id
        else:
            container = container_id

        # Get the metatype information
        metatype_info = self.deep_lynx.list_metatypes(container, params)
        if metatype_info['isError'] == False and len(metatype_info["value"]) > 0:
            info = metatype_info["value"][0]
            # Add {property: datatype} to dictionary
            properties = info["keys"]
            metatype_properties = dict()
            for property in properties:
                metatype_properties[property["name"]] = property["data_type"]
            error["value"] = metatype_properties
        else:
            error["isError"] = True
            error["error"].append("The metatype '{0}' does not exist".format(metatype))
        error = json.dumps(error)
        return error

    def __identify_datatype(self, value):
        """
        Identifies whether the provided value is 'string', 'number', 'boolean', 'date', or 'file'
        Args:
            value: the item to check its datatype
        """
        dtype = ""
        if isinstance(value, bool):
            dtype = 'boolean'
        elif isinstance(value, int) or isinstance(value, float):
            dtype = 'number'
        elif isinstance(value, str):
            if os.path.isfile(value):
                dtype = 'file'
            if len(value) > 0:
                try:
                    if value[-1] == 'Z':
                        date = datetime.datetime.fromisoformat(value[:-1])
                    else:
                        date = datetime.datetime.fromisoformat(value)
                    if isinstance(date, datetime.date):
                        dtype = 'date'
                except ValueError:
                    pass
            if not dtype:
                dtype = "string"
        return dtype
