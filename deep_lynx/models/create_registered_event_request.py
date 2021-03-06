# coding: utf-8

"""
    Deep Lynx

    The construction of megaprojects has consistently demonstrated challenges for project managers in regard to meeting cost, schedule, and performance requirements. Megaproject construction challenges are common place within megaprojects with many active projects in the United States failing to meet cost and schedule efforts by significant margins. Currently, engineering teams operate in siloed tools and disparate teams where connections across design, procurement, and construction systems are translated manually or over brittle point-to-point integrations. The manual nature of data exchange increases the risk of silent errors in the reactor design, with each silent error cascading across the design. These cascading errors lead to uncontrollable risk during construction, resulting in significant delays and cost overruns. Deep Lynx allows for an integrated platform during design and operations of mega projects.  The Deep Lynx Core API delivers a few main features.  1. Provides a set of methods and endpoints for manipulating data in an object oriented database. This allows us to store complex datatypes as records and then to compile them into actual, modifiable objects at run-time. Users can store taxonomies or ontologies in a readable format.  2. Provides methods for storing and retrieving data in a graph database. This data is structured and validated against the aformentioned object oriented database before storage.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateRegisteredEventRequest(object):
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
        'app_name': 'str',
        'app_url': 'str',
        'container_id': 'str',
        'event_type': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_url': 'app_url',
        'container_id': 'container_id',
        'event_type': 'event_type'
    }

    def __init__(self, app_name=None, app_url=None, container_id=None, event_type=None):  # noqa: E501
        """CreateRegisteredEventRequest - a model defined in Swagger"""  # noqa: E501
        self._app_name = None
        self._app_url = None
        self._container_id = None
        self._event_type = None
        self.discriminator = None
        self.app_name = app_name
        self.app_url = app_url
        self.container_id = container_id
        self.event_type = event_type

    @property
    def app_name(self):
        """Gets the app_name of this CreateRegisteredEventRequest.  # noqa: E501


        :return: The app_name of this CreateRegisteredEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this CreateRegisteredEventRequest.


        :param app_name: The app_name of this CreateRegisteredEventRequest.  # noqa: E501
        :type: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def app_url(self):
        """Gets the app_url of this CreateRegisteredEventRequest.  # noqa: E501


        :return: The app_url of this CreateRegisteredEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this CreateRegisteredEventRequest.


        :param app_url: The app_url of this CreateRegisteredEventRequest.  # noqa: E501
        :type: str
        """
        if app_url is None:
            raise ValueError("Invalid value for `app_url`, must not be `None`")  # noqa: E501

        self._app_url = app_url

    @property
    def container_id(self):
        """Gets the container_id of this CreateRegisteredEventRequest.  # noqa: E501


        :return: The container_id of this CreateRegisteredEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this CreateRegisteredEventRequest.


        :param container_id: The container_id of this CreateRegisteredEventRequest.  # noqa: E501
        :type: str
        """
        if container_id is None:
            raise ValueError("Invalid value for `container_id`, must not be `None`")  # noqa: E501

        self._container_id = container_id

    @property
    def event_type(self):
        """Gets the event_type of this CreateRegisteredEventRequest.  # noqa: E501


        :return: The event_type of this CreateRegisteredEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this CreateRegisteredEventRequest.


        :param event_type: The event_type of this CreateRegisteredEventRequest.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

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
        if issubclass(CreateRegisteredEventRequest, dict):
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
        if not isinstance(other, CreateRegisteredEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
