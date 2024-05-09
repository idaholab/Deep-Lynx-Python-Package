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

class Task(object):
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
        'id': 'str',
        'container_id': 'str',
        'task_type': 'str',
        'status': 'str',
        'query': 'str',
        'data': 'object',
        'config': 'TaskConfig',
        'status_message': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'container_id': 'container_id',
        'task_type': 'task_type',
        'status': 'status',
        'query': 'query',
        'data': 'data',
        'config': 'config',
        'status_message': 'status_message',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, container_id=None, task_type=None, status=None, query=None, data=None, config=None, status_message=None, created_at=None, modified_at=None, created_by=None, modified_by=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._container_id = None
        self._task_type = None
        self._status = None
        self._query = None
        self._data = None
        self._config = None
        self._status_message = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if container_id is not None:
            self.container_id = container_id
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if query is not None:
            self.query = query
        if data is not None:
            self.data = data
        if config is not None:
            self.config = config
        if status_message is not None:
            self.status_message = status_message
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501


        :return: The id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.


        :param id: The id of this Task.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def container_id(self):
        """Gets the container_id of this Task.  # noqa: E501


        :return: The container_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this Task.


        :param container_id: The container_id of this Task.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def task_type(self):
        """Gets the task_type of this Task.  # noqa: E501


        :return: The task_type of this Task.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this Task.


        :param task_type: The task_type of this Task.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501


        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.


        :param status: The status of this Task.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def query(self):
        """Gets the query of this Task.  # noqa: E501


        :return: The query of this Task.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Task.


        :param query: The query of this Task.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def data(self):
        """Gets the data of this Task.  # noqa: E501


        :return: The data of this Task.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Task.


        :param data: The data of this Task.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def config(self):
        """Gets the config of this Task.  # noqa: E501


        :return: The config of this Task.  # noqa: E501
        :rtype: TaskConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Task.


        :param config: The config of this Task.  # noqa: E501
        :type: TaskConfig
        """

        self._config = config

    @property
    def status_message(self):
        """Gets the status_message of this Task.  # noqa: E501


        :return: The status_message of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this Task.


        :param status_message: The status_message of this Task.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def created_at(self):
        """Gets the created_at of this Task.  # noqa: E501


        :return: The created_at of this Task.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Task.


        :param created_at: The created_at of this Task.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Task.  # noqa: E501


        :return: The modified_at of this Task.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Task.


        :param modified_at: The modified_at of this Task.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this Task.  # noqa: E501


        :return: The created_by of this Task.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Task.


        :param created_by: The created_by of this Task.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Task.  # noqa: E501


        :return: The modified_by of this Task.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Task.


        :param modified_by: The modified_by of this Task.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

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
        if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
