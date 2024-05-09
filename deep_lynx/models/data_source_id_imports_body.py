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

class DataSourceIdImportsBody(object):
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
        'data_source_id': 'str',
        'reference': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'data_source_id': 'data_source_id',
        'reference': 'reference',
        'status_message': 'status_message'
    }

    def __init__(self, data_source_id=None, reference=None, status_message=None):  # noqa: E501
        """DataSourceIdImportsBody - a model defined in Swagger"""  # noqa: E501
        self._data_source_id = None
        self._reference = None
        self._status_message = None
        self.discriminator = None
        self.data_source_id = data_source_id
        if reference is not None:
            self.reference = reference
        if status_message is not None:
            self.status_message = status_message

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DataSourceIdImportsBody.  # noqa: E501


        :return: The data_source_id of this DataSourceIdImportsBody.  # noqa: E501
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DataSourceIdImportsBody.


        :param data_source_id: The data_source_id of this DataSourceIdImportsBody.  # noqa: E501
        :type: str
        """
        if data_source_id is None:
            raise ValueError("Invalid value for `data_source_id`, must not be `None`")  # noqa: E501

        self._data_source_id = data_source_id

    @property
    def reference(self):
        """Gets the reference of this DataSourceIdImportsBody.  # noqa: E501


        :return: The reference of this DataSourceIdImportsBody.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DataSourceIdImportsBody.


        :param reference: The reference of this DataSourceIdImportsBody.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def status_message(self):
        """Gets the status_message of this DataSourceIdImportsBody.  # noqa: E501


        :return: The status_message of this DataSourceIdImportsBody.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this DataSourceIdImportsBody.


        :param status_message: The status_message of this DataSourceIdImportsBody.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

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
        if issubclass(DataSourceIdImportsBody, dict):
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
        if not isinstance(other, DataSourceIdImportsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
