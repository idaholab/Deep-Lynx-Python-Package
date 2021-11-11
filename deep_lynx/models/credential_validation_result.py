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

class CredentialValidationResult(object):
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
        'method_id': 'str',
        'method_response_code': 'str',
        'method_reason_code': 'str',
        'authn_attributes': 'list[str]'
    }

    attribute_map = {
        'method_id': 'methodId',
        'method_response_code': 'methodResponseCode',
        'method_reason_code': 'methodReasonCode',
        'authn_attributes': 'authnAttributes'
    }

    def __init__(self, method_id=None, method_response_code=None, method_reason_code=None, authn_attributes=None):  # noqa: E501
        """CredentialValidationResult - a model defined in Swagger"""  # noqa: E501
        self._method_id = None
        self._method_response_code = None
        self._method_reason_code = None
        self._authn_attributes = None
        self.discriminator = None
        if method_id is not None:
            self.method_id = method_id
        if method_response_code is not None:
            self.method_response_code = method_response_code
        if method_reason_code is not None:
            self.method_reason_code = method_reason_code
        if authn_attributes is not None:
            self.authn_attributes = authn_attributes

    @property
    def method_id(self):
        """Gets the method_id of this CredentialValidationResult.  # noqa: E501


        :return: The method_id of this CredentialValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this CredentialValidationResult.


        :param method_id: The method_id of this CredentialValidationResult.  # noqa: E501
        :type: str
        """

        self._method_id = method_id

    @property
    def method_response_code(self):
        """Gets the method_response_code of this CredentialValidationResult.  # noqa: E501


        :return: The method_response_code of this CredentialValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._method_response_code

    @method_response_code.setter
    def method_response_code(self, method_response_code):
        """Sets the method_response_code of this CredentialValidationResult.


        :param method_response_code: The method_response_code of this CredentialValidationResult.  # noqa: E501
        :type: str
        """

        self._method_response_code = method_response_code

    @property
    def method_reason_code(self):
        """Gets the method_reason_code of this CredentialValidationResult.  # noqa: E501


        :return: The method_reason_code of this CredentialValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._method_reason_code

    @method_reason_code.setter
    def method_reason_code(self, method_reason_code):
        """Sets the method_reason_code of this CredentialValidationResult.


        :param method_reason_code: The method_reason_code of this CredentialValidationResult.  # noqa: E501
        :type: str
        """

        self._method_reason_code = method_reason_code

    @property
    def authn_attributes(self):
        """Gets the authn_attributes of this CredentialValidationResult.  # noqa: E501


        :return: The authn_attributes of this CredentialValidationResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._authn_attributes

    @authn_attributes.setter
    def authn_attributes(self, authn_attributes):
        """Sets the authn_attributes of this CredentialValidationResult.


        :param authn_attributes: The authn_attributes of this CredentialValidationResult.  # noqa: E501
        :type: list[str]
        """

        self._authn_attributes = authn_attributes

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
        if issubclass(CredentialValidationResult, dict):
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
        if not isinstance(other, CredentialValidationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
