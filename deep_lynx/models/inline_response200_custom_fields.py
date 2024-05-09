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

class InlineResponse200CustomFields(object):
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
        'name': 'str',
        'value': 'str',
        'encrypt': 'bool',
        'required': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'encrypt': 'encrypt',
        'required': 'required'
    }

    def __init__(self, name=None, value=None, encrypt=None, required=None):  # noqa: E501
        """InlineResponse200CustomFields - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self._encrypt = None
        self._required = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if encrypt is not None:
            self.encrypt = encrypt
        if required is not None:
            self.required = required

    @property
    def name(self):
        """Gets the name of this InlineResponse200CustomFields.  # noqa: E501


        :return: The name of this InlineResponse200CustomFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200CustomFields.


        :param name: The name of this InlineResponse200CustomFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this InlineResponse200CustomFields.  # noqa: E501


        :return: The value of this InlineResponse200CustomFields.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse200CustomFields.


        :param value: The value of this InlineResponse200CustomFields.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def encrypt(self):
        """Gets the encrypt of this InlineResponse200CustomFields.  # noqa: E501


        :return: The encrypt of this InlineResponse200CustomFields.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt

    @encrypt.setter
    def encrypt(self, encrypt):
        """Sets the encrypt of this InlineResponse200CustomFields.


        :param encrypt: The encrypt of this InlineResponse200CustomFields.  # noqa: E501
        :type: bool
        """

        self._encrypt = encrypt

    @property
    def required(self):
        """Gets the required of this InlineResponse200CustomFields.  # noqa: E501


        :return: The required of this InlineResponse200CustomFields.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this InlineResponse200CustomFields.


        :param required: The required of this InlineResponse200CustomFields.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(InlineResponse200CustomFields, dict):
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
        if not isinstance(other, InlineResponse200CustomFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
