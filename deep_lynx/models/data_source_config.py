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

class DataSourceConfig(object):
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
        'kind': 'str',
        'data_type': 'str',
        'data_format': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'data_type': 'data_type',
        'data_format': 'data_format'
    }

    def __init__(self, kind=None, data_type=None, data_format=None):  # noqa: E501
        """DataSourceConfig - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._data_type = None
        self._data_format = None
        self.discriminator = None
        if kind is not None:
            self.kind = kind
        if data_type is not None:
            self.data_type = data_type
        if data_format is not None:
            self.data_format = data_format

    @property
    def kind(self):
        """Gets the kind of this DataSourceConfig.  # noqa: E501


        :return: The kind of this DataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this DataSourceConfig.


        :param kind: The kind of this DataSourceConfig.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def data_type(self):
        """Gets the data_type of this DataSourceConfig.  # noqa: E501


        :return: The data_type of this DataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataSourceConfig.


        :param data_type: The data_type of this DataSourceConfig.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def data_format(self):
        """Gets the data_format of this DataSourceConfig.  # noqa: E501


        :return: The data_format of this DataSourceConfig.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this DataSourceConfig.


        :param data_format: The data_format of this DataSourceConfig.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

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
        if issubclass(DataSourceConfig, dict):
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
        if not isinstance(other, DataSourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other