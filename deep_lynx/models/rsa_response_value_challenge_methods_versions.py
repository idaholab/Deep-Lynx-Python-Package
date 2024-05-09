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

class RSAResponseValueChallengeMethodsVersions(object):
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
        'version_id': 'str',
        'method_attributes': 'list[str]',
        'value_required': 'bool',
        'reference_id': 'str',
        'prompt': 'RSAResponseValueChallengeMethodsPrompt'
    }

    attribute_map = {
        'version_id': 'versionId',
        'method_attributes': 'methodAttributes',
        'value_required': 'valueRequired',
        'reference_id': 'referenceId',
        'prompt': 'prompt'
    }

    def __init__(self, version_id=None, method_attributes=None, value_required=None, reference_id=None, prompt=None):  # noqa: E501
        """RSAResponseValueChallengeMethodsVersions - a model defined in Swagger"""  # noqa: E501
        self._version_id = None
        self._method_attributes = None
        self._value_required = None
        self._reference_id = None
        self._prompt = None
        self.discriminator = None
        if version_id is not None:
            self.version_id = version_id
        if method_attributes is not None:
            self.method_attributes = method_attributes
        if value_required is not None:
            self.value_required = value_required
        if reference_id is not None:
            self.reference_id = reference_id
        if prompt is not None:
            self.prompt = prompt

    @property
    def version_id(self):
        """Gets the version_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501


        :return: The version_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this RSAResponseValueChallengeMethodsVersions.


        :param version_id: The version_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def method_attributes(self):
        """Gets the method_attributes of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501


        :return: The method_attributes of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :rtype: list[str]
        """
        return self._method_attributes

    @method_attributes.setter
    def method_attributes(self, method_attributes):
        """Sets the method_attributes of this RSAResponseValueChallengeMethodsVersions.


        :param method_attributes: The method_attributes of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :type: list[str]
        """

        self._method_attributes = method_attributes

    @property
    def value_required(self):
        """Gets the value_required of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501


        :return: The value_required of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :rtype: bool
        """
        return self._value_required

    @value_required.setter
    def value_required(self, value_required):
        """Sets the value_required of this RSAResponseValueChallengeMethodsVersions.


        :param value_required: The value_required of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :type: bool
        """

        self._value_required = value_required

    @property
    def reference_id(self):
        """Gets the reference_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501


        :return: The reference_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this RSAResponseValueChallengeMethodsVersions.


        :param reference_id: The reference_id of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def prompt(self):
        """Gets the prompt of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501


        :return: The prompt of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :rtype: RSAResponseValueChallengeMethodsPrompt
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this RSAResponseValueChallengeMethodsVersions.


        :param prompt: The prompt of this RSAResponseValueChallengeMethodsVersions.  # noqa: E501
        :type: RSAResponseValueChallengeMethodsPrompt
        """

        self._prompt = prompt

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
        if issubclass(RSAResponseValueChallengeMethodsVersions, dict):
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
        if not isinstance(other, RSAResponseValueChallengeMethodsVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
