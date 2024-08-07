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

class CreateDataSourceConfig(object):
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
        'endpoint': 'str',
        'auth_method': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'auth_method': 'auth_method',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, endpoint=None, auth_method=None, username=None, password=None):  # noqa: E501
        """CreateDataSourceConfig - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._auth_method = None
        self._username = None
        self._password = None
        self.discriminator = None
        if endpoint is not None:
            self.endpoint = endpoint
        if auth_method is not None:
            self.auth_method = auth_method
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def endpoint(self):
        """Gets the endpoint of this CreateDataSourceConfig.  # noqa: E501


        :return: The endpoint of this CreateDataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this CreateDataSourceConfig.


        :param endpoint: The endpoint of this CreateDataSourceConfig.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def auth_method(self):
        """Gets the auth_method of this CreateDataSourceConfig.  # noqa: E501


        :return: The auth_method of this CreateDataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this CreateDataSourceConfig.


        :param auth_method: The auth_method of this CreateDataSourceConfig.  # noqa: E501
        :type: str
        """

        self._auth_method = auth_method

    @property
    def username(self):
        """Gets the username of this CreateDataSourceConfig.  # noqa: E501


        :return: The username of this CreateDataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateDataSourceConfig.


        :param username: The username of this CreateDataSourceConfig.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this CreateDataSourceConfig.  # noqa: E501


        :return: The password of this CreateDataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateDataSourceConfig.


        :param password: The password of this CreateDataSourceConfig.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(CreateDataSourceConfig, dict):
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
        if not isinstance(other, CreateDataSourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
