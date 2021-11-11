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

class FileModel(object):
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
        'status': 'str',
        'id': 'str',
        'data_source_id': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'reference': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'data_source_id': 'data_source_id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'reference': 'reference',
        'status_message': 'status_message'
    }

    def __init__(self, status=None, id=None, data_source_id=None, created_at=None, modified_at=None, created_by=None, modified_by=None, reference=None, status_message=None):  # noqa: E501
        """FileModel - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._id = None
        self._data_source_id = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._reference = None
        self._status_message = None
        self.discriminator = None
        self.status = status
        self.id = id
        self.data_source_id = data_source_id
        self.created_at = created_at
        self.modified_at = modified_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.reference = reference
        if status_message is not None:
            self.status_message = status_message

    @property
    def status(self):
        """Gets the status of this FileModel.  # noqa: E501


        :return: The status of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileModel.


        :param status: The status of this FileModel.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def id(self):
        """Gets the id of this FileModel.  # noqa: E501


        :return: The id of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileModel.


        :param id: The id of this FileModel.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def data_source_id(self):
        """Gets the data_source_id of this FileModel.  # noqa: E501


        :return: The data_source_id of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this FileModel.


        :param data_source_id: The data_source_id of this FileModel.  # noqa: E501
        :type: str
        """
        if data_source_id is None:
            raise ValueError("Invalid value for `data_source_id`, must not be `None`")  # noqa: E501

        self._data_source_id = data_source_id

    @property
    def created_at(self):
        """Gets the created_at of this FileModel.  # noqa: E501


        :return: The created_at of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileModel.


        :param created_at: The created_at of this FileModel.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this FileModel.  # noqa: E501


        :return: The modified_at of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this FileModel.


        :param modified_at: The modified_at of this FileModel.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this FileModel.  # noqa: E501


        :return: The created_by of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FileModel.


        :param created_by: The created_by of this FileModel.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this FileModel.  # noqa: E501


        :return: The modified_by of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this FileModel.


        :param modified_by: The modified_by of this FileModel.  # noqa: E501
        :type: str
        """
        if modified_by is None:
            raise ValueError("Invalid value for `modified_by`, must not be `None`")  # noqa: E501

        self._modified_by = modified_by

    @property
    def reference(self):
        """Gets the reference of this FileModel.  # noqa: E501


        :return: The reference of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this FileModel.


        :param reference: The reference of this FileModel.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def status_message(self):
        """Gets the status_message of this FileModel.  # noqa: E501


        :return: The status_message of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this FileModel.


        :param status_message: The status_message of this FileModel.  # noqa: E501
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
        if issubclass(FileModel, dict):
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
        if not isinstance(other, FileModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
