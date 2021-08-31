import os
import json
import logging
import datetime
import settings

from deep_lynx.deep_lynx_service import DeepLynxService


class DeepLynxValidator():
    def __init__(self, deep_lynx: DeepLynxService):
        """Initializes a Deep Lynx Service object."""
        self.deep_lynx: str = deep_lynx

    def validate_properties(self, metatype: str, json_data: dict, container_id: str = None):
        error = dict()
        error["isError"] = False
        error["error"] = list()

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

    def __get_properties(self, metatype: str, container_id: str = None):
        error = dict()
        error["isError"] = False
        error["error"] = list()
        error["value"] = None

        params = {"name": metatype}
        if not container_id:
            container = self.deep_lynx.container_id
        else:
            container = container_id
        print(container_id)
        metatype_info = self.deep_lynx.list_metatypes(container, params)
        print(metatype_info)
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
        Inputs:
                value: the item to check its datatype
        Outputs:
                dtype: the datatype either 'string', 'number', 'boolean', 'date', or 'file'
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
