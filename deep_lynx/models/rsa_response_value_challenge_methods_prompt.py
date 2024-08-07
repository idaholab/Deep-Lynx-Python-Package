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

class RSAResponseValueChallengeMethodsPrompt(object):
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
        'prompt_resource_id': 'str',
        'default_text': 'str',
        'format_regex': 'str',
        'default_value': 'str',
        'value_being_defined': 'bool',
        'sensitive': 'bool',
        'min_length': 'str',
        'max_length': 'str',
        'prompt_args': 'list[str]'
    }

    attribute_map = {
        'prompt_resource_id': 'promptResourceId',
        'default_text': 'defaultText',
        'format_regex': 'formatRegex',
        'default_value': 'defaultValue',
        'value_being_defined': 'valueBeingDefined',
        'sensitive': 'sensitive',
        'min_length': 'minLength',
        'max_length': 'maxLength',
        'prompt_args': 'promptArgs'
    }

    def __init__(self, prompt_resource_id=None, default_text=None, format_regex=None, default_value=None, value_being_defined=None, sensitive=None, min_length=None, max_length=None, prompt_args=None):  # noqa: E501
        """RSAResponseValueChallengeMethodsPrompt - a model defined in Swagger"""  # noqa: E501
        self._prompt_resource_id = None
        self._default_text = None
        self._format_regex = None
        self._default_value = None
        self._value_being_defined = None
        self._sensitive = None
        self._min_length = None
        self._max_length = None
        self._prompt_args = None
        self.discriminator = None
        if prompt_resource_id is not None:
            self.prompt_resource_id = prompt_resource_id
        if default_text is not None:
            self.default_text = default_text
        if format_regex is not None:
            self.format_regex = format_regex
        if default_value is not None:
            self.default_value = default_value
        if value_being_defined is not None:
            self.value_being_defined = value_being_defined
        if sensitive is not None:
            self.sensitive = sensitive
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        if prompt_args is not None:
            self.prompt_args = prompt_args

    @property
    def prompt_resource_id(self):
        """Gets the prompt_resource_id of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The prompt_resource_id of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._prompt_resource_id

    @prompt_resource_id.setter
    def prompt_resource_id(self, prompt_resource_id):
        """Sets the prompt_resource_id of this RSAResponseValueChallengeMethodsPrompt.


        :param prompt_resource_id: The prompt_resource_id of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._prompt_resource_id = prompt_resource_id

    @property
    def default_text(self):
        """Gets the default_text of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The default_text of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._default_text

    @default_text.setter
    def default_text(self, default_text):
        """Sets the default_text of this RSAResponseValueChallengeMethodsPrompt.


        :param default_text: The default_text of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._default_text = default_text

    @property
    def format_regex(self):
        """Gets the format_regex of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The format_regex of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._format_regex

    @format_regex.setter
    def format_regex(self, format_regex):
        """Sets the format_regex of this RSAResponseValueChallengeMethodsPrompt.


        :param format_regex: The format_regex of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._format_regex = format_regex

    @property
    def default_value(self):
        """Gets the default_value of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The default_value of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this RSAResponseValueChallengeMethodsPrompt.


        :param default_value: The default_value of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def value_being_defined(self):
        """Gets the value_being_defined of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The value_being_defined of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: bool
        """
        return self._value_being_defined

    @value_being_defined.setter
    def value_being_defined(self, value_being_defined):
        """Sets the value_being_defined of this RSAResponseValueChallengeMethodsPrompt.


        :param value_being_defined: The value_being_defined of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: bool
        """

        self._value_being_defined = value_being_defined

    @property
    def sensitive(self):
        """Gets the sensitive of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The sensitive of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this RSAResponseValueChallengeMethodsPrompt.


        :param sensitive: The sensitive of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def min_length(self):
        """Gets the min_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The min_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this RSAResponseValueChallengeMethodsPrompt.


        :param min_length: The min_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The max_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: str
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this RSAResponseValueChallengeMethodsPrompt.


        :param max_length: The max_length of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: str
        """

        self._max_length = max_length

    @property
    def prompt_args(self):
        """Gets the prompt_args of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501


        :return: The prompt_args of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :rtype: list[str]
        """
        return self._prompt_args

    @prompt_args.setter
    def prompt_args(self, prompt_args):
        """Sets the prompt_args of this RSAResponseValueChallengeMethodsPrompt.


        :param prompt_args: The prompt_args of this RSAResponseValueChallengeMethodsPrompt.  # noqa: E501
        :type: list[str]
        """

        self._prompt_args = prompt_args

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
        if issubclass(RSAResponseValueChallengeMethodsPrompt, dict):
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
        if not isinstance(other, RSAResponseValueChallengeMethodsPrompt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
