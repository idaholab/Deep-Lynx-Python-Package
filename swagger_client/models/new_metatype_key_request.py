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

class NewMetatypeKeyRequest(object):
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
        'required': 'bool',
        'property_name': 'str',
        'description': 'str',
        'data_type': 'str',
        'cardinality': 'int',
        'validation': 'KeyValidation',
        'unique': 'bool',
        'options': 'list[str]',
        'default_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'required': 'required',
        'property_name': 'property_name',
        'description': 'description',
        'data_type': 'data_type',
        'cardinality': 'cardinality',
        'validation': 'validation',
        'unique': 'unique',
        'options': 'options',
        'default_value': 'defaultValue'
    }

    def __init__(self, name=None, required=None, property_name=None, description=None, data_type=None, cardinality=None, validation=None, unique=None, options=None, default_value=None):  # noqa: E501
        """NewMetatypeKeyRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._required = None
        self._property_name = None
        self._description = None
        self._data_type = None
        self._cardinality = None
        self._validation = None
        self._unique = None
        self._options = None
        self._default_value = None
        self.discriminator = None
        self.name = name
        self.required = required
        self.property_name = property_name
        self.description = description
        self.data_type = data_type
        self.cardinality = cardinality
        self.validation = validation
        self.unique = unique
        self.options = options
        self.default_value = default_value

    @property
    def name(self):
        """Gets the name of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The name of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewMetatypeKeyRequest.


        :param name: The name of this NewMetatypeKeyRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def required(self):
        """Gets the required of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The required of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this NewMetatypeKeyRequest.


        :param required: The required of this NewMetatypeKeyRequest.  # noqa: E501
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def property_name(self):
        """Gets the property_name of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The property_name of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this NewMetatypeKeyRequest.


        :param property_name: The property_name of this NewMetatypeKeyRequest.  # noqa: E501
        :type: str
        """
        if property_name is None:
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501

        self._property_name = property_name

    @property
    def description(self):
        """Gets the description of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The description of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewMetatypeKeyRequest.


        :param description: The description of this NewMetatypeKeyRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The data_type of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this NewMetatypeKeyRequest.


        :param data_type: The data_type of this NewMetatypeKeyRequest.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def cardinality(self):
        """Gets the cardinality of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The cardinality of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: int
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this NewMetatypeKeyRequest.


        :param cardinality: The cardinality of this NewMetatypeKeyRequest.  # noqa: E501
        :type: int
        """
        if cardinality is None:
            raise ValueError("Invalid value for `cardinality`, must not be `None`")  # noqa: E501

        self._cardinality = cardinality

    @property
    def validation(self):
        """Gets the validation of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The validation of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: KeyValidation
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this NewMetatypeKeyRequest.


        :param validation: The validation of this NewMetatypeKeyRequest.  # noqa: E501
        :type: KeyValidation
        """
        if validation is None:
            raise ValueError("Invalid value for `validation`, must not be `None`")  # noqa: E501

        self._validation = validation

    @property
    def unique(self):
        """Gets the unique of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The unique of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this NewMetatypeKeyRequest.


        :param unique: The unique of this NewMetatypeKeyRequest.  # noqa: E501
        :type: bool
        """
        if unique is None:
            raise ValueError("Invalid value for `unique`, must not be `None`")  # noqa: E501

        self._unique = unique

    @property
    def options(self):
        """Gets the options of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The options of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this NewMetatypeKeyRequest.


        :param options: The options of this NewMetatypeKeyRequest.  # noqa: E501
        :type: list[str]
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def default_value(self):
        """Gets the default_value of this NewMetatypeKeyRequest.  # noqa: E501


        :return: The default_value of this NewMetatypeKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this NewMetatypeKeyRequest.


        :param default_value: The default_value of this NewMetatypeKeyRequest.  # noqa: E501
        :type: str
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")  # noqa: E501

        self._default_value = default_value

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
        if issubclass(NewMetatypeKeyRequest, dict):
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
        if not isinstance(other, NewMetatypeKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
