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

class DataTarget(object):
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
        'adapter_type': 'str',
        'status': 'str',
        'active': 'bool',
        'config': 'DataTargetConfig',
        'id': 'str',
        'container_id': 'str',
        'name': 'str',
        'data_format': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'archived': 'bool',
        'status_message': 'str'
    }

    attribute_map = {
        'adapter_type': 'adapter_type',
        'status': 'status',
        'active': 'active',
        'config': 'config',
        'id': 'id',
        'container_id': 'container_id',
        'name': 'name',
        'data_format': 'data_format',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'archived': 'archived',
        'status_message': 'status_message'
    }

    def __init__(self, adapter_type=None, status=None, active=None, config=None, id=None, container_id=None, name=None, data_format=None, created_at=None, modified_at=None, created_by=None, modified_by=None, archived=None, status_message=None):  # noqa: E501
        """DataTarget - a model defined in Swagger"""  # noqa: E501
        self._adapter_type = None
        self._status = None
        self._active = None
        self._config = None
        self._id = None
        self._container_id = None
        self._name = None
        self._data_format = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._archived = None
        self._status_message = None
        self.discriminator = None
        self.adapter_type = adapter_type
        if status is not None:
            self.status = status
        self.active = active
        if config is not None:
            self.config = config
        if id is not None:
            self.id = id
        self.container_id = container_id
        self.name = name
        if data_format is not None:
            self.data_format = data_format
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if archived is not None:
            self.archived = archived
        if status_message is not None:
            self.status_message = status_message

    @property
    def adapter_type(self):
        """Gets the adapter_type of this DataTarget.  # noqa: E501


        :return: The adapter_type of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._adapter_type

    @adapter_type.setter
    def adapter_type(self, adapter_type):
        """Sets the adapter_type of this DataTarget.


        :param adapter_type: The adapter_type of this DataTarget.  # noqa: E501
        :type: str
        """
        if adapter_type is None:
            raise ValueError("Invalid value for `adapter_type`, must not be `None`")  # noqa: E501

        self._adapter_type = adapter_type

    @property
    def status(self):
        """Gets the status of this DataTarget.  # noqa: E501


        :return: The status of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataTarget.


        :param status: The status of this DataTarget.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def active(self):
        """Gets the active of this DataTarget.  # noqa: E501


        :return: The active of this DataTarget.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DataTarget.


        :param active: The active of this DataTarget.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def config(self):
        """Gets the config of this DataTarget.  # noqa: E501


        :return: The config of this DataTarget.  # noqa: E501
        :rtype: DataTargetConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this DataTarget.


        :param config: The config of this DataTarget.  # noqa: E501
        :type: DataTargetConfig
        """

        self._config = config

    @property
    def id(self):
        """Gets the id of this DataTarget.  # noqa: E501


        :return: The id of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataTarget.


        :param id: The id of this DataTarget.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def container_id(self):
        """Gets the container_id of this DataTarget.  # noqa: E501


        :return: The container_id of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this DataTarget.


        :param container_id: The container_id of this DataTarget.  # noqa: E501
        :type: str
        """
        if container_id is None:
            raise ValueError("Invalid value for `container_id`, must not be `None`")  # noqa: E501

        self._container_id = container_id

    @property
    def name(self):
        """Gets the name of this DataTarget.  # noqa: E501


        :return: The name of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataTarget.


        :param name: The name of this DataTarget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def data_format(self):
        """Gets the data_format of this DataTarget.  # noqa: E501


        :return: The data_format of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this DataTarget.


        :param data_format: The data_format of this DataTarget.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def created_at(self):
        """Gets the created_at of this DataTarget.  # noqa: E501


        :return: The created_at of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataTarget.


        :param created_at: The created_at of this DataTarget.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this DataTarget.  # noqa: E501


        :return: The modified_at of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this DataTarget.


        :param modified_at: The modified_at of this DataTarget.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this DataTarget.  # noqa: E501


        :return: The created_by of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DataTarget.


        :param created_by: The created_by of this DataTarget.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this DataTarget.  # noqa: E501


        :return: The modified_by of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this DataTarget.


        :param modified_by: The modified_by of this DataTarget.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def archived(self):
        """Gets the archived of this DataTarget.  # noqa: E501


        :return: The archived of this DataTarget.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this DataTarget.


        :param archived: The archived of this DataTarget.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def status_message(self):
        """Gets the status_message of this DataTarget.  # noqa: E501


        :return: The status_message of this DataTarget.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this DataTarget.


        :param status_message: The status_message of this DataTarget.  # noqa: E501
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
        if issubclass(DataTarget, dict):
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
        if not isinstance(other, DataTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
