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

class CreateEventRequest(object):
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
        'container_id': 'str',
        'data_source_id': 'str',
        'event_type': 'str',
        'event_config': 'object',
        'event': 'object'
    }

    attribute_map = {
        'container_id': 'container_id',
        'data_source_id': 'data_source_id',
        'event_type': 'event_type',
        'event_config': 'event_config',
        'event': 'event'
    }

    def __init__(self, container_id=None, data_source_id=None, event_type=None, event_config=None, event=None):  # noqa: E501
        """CreateEventRequest - a model defined in Swagger"""  # noqa: E501
        self._container_id = None
        self._data_source_id = None
        self._event_type = None
        self._event_config = None
        self._event = None
        self.discriminator = None
        if container_id is not None:
            self.container_id = container_id
        if data_source_id is not None:
            self.data_source_id = data_source_id
        self.event_type = event_type
        if event_config is not None:
            self.event_config = event_config
        self.event = event

    @property
    def container_id(self):
        """Gets the container_id of this CreateEventRequest.  # noqa: E501


        :return: The container_id of this CreateEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this CreateEventRequest.


        :param container_id: The container_id of this CreateEventRequest.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def data_source_id(self):
        """Gets the data_source_id of this CreateEventRequest.  # noqa: E501


        :return: The data_source_id of this CreateEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this CreateEventRequest.


        :param data_source_id: The data_source_id of this CreateEventRequest.  # noqa: E501
        :type: str
        """

        self._data_source_id = data_source_id

    @property
    def event_type(self):
        """Gets the event_type of this CreateEventRequest.  # noqa: E501


        :return: The event_type of this CreateEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this CreateEventRequest.


        :param event_type: The event_type of this CreateEventRequest.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def event_config(self):
        """Gets the event_config of this CreateEventRequest.  # noqa: E501


        :return: The event_config of this CreateEventRequest.  # noqa: E501
        :rtype: object
        """
        return self._event_config

    @event_config.setter
    def event_config(self, event_config):
        """Sets the event_config of this CreateEventRequest.


        :param event_config: The event_config of this CreateEventRequest.  # noqa: E501
        :type: object
        """

        self._event_config = event_config

    @property
    def event(self):
        """Gets the event of this CreateEventRequest.  # noqa: E501


        :return: The event of this CreateEventRequest.  # noqa: E501
        :rtype: object
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this CreateEventRequest.


        :param event: The event of this CreateEventRequest.  # noqa: E501
        :type: object
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

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
        if issubclass(CreateEventRequest, dict):
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
        if not isinstance(other, CreateEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
