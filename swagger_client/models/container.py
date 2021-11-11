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

class Container(object):
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
        'description': 'str',
        'id': 'str',
        'archived': 'bool',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'config': 'ContainerConfig',
        'active_graph_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'archived': 'archived',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'config': 'config',
        'active_graph_id': 'active_graph_id'
    }

    def __init__(self, name=None, description=None, id=None, archived=None, created_at=None, modified_at=None, created_by=None, modified_by=None, config=None, active_graph_id=None):  # noqa: E501
        """Container - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._archived = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._config = None
        self._active_graph_id = None
        self.discriminator = None
        self.name = name
        self.description = description
        self.id = id
        self.archived = archived
        self.created_at = created_at
        self.modified_at = modified_at
        self.created_by = created_by
        self.modified_by = modified_by
        if config is not None:
            self.config = config
        self.active_graph_id = active_graph_id

    @property
    def name(self):
        """Gets the name of this Container.  # noqa: E501


        :return: The name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Container.


        :param name: The name of this Container.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Container.  # noqa: E501


        :return: The description of this Container.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Container.


        :param description: The description of this Container.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Container.  # noqa: E501


        :return: The id of this Container.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Container.


        :param id: The id of this Container.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def archived(self):
        """Gets the archived of this Container.  # noqa: E501


        :return: The archived of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Container.


        :param archived: The archived of this Container.  # noqa: E501
        :type: bool
        """
        if archived is None:
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def created_at(self):
        """Gets the created_at of this Container.  # noqa: E501


        :return: The created_at of this Container.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Container.


        :param created_at: The created_at of this Container.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Container.  # noqa: E501


        :return: The modified_at of this Container.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Container.


        :param modified_at: The modified_at of this Container.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this Container.  # noqa: E501


        :return: The created_by of this Container.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Container.


        :param created_by: The created_by of this Container.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Container.  # noqa: E501


        :return: The modified_by of this Container.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Container.


        :param modified_by: The modified_by of this Container.  # noqa: E501
        :type: str
        """
        if modified_by is None:
            raise ValueError("Invalid value for `modified_by`, must not be `None`")  # noqa: E501

        self._modified_by = modified_by

    @property
    def config(self):
        """Gets the config of this Container.  # noqa: E501


        :return: The config of this Container.  # noqa: E501
        :rtype: ContainerConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Container.


        :param config: The config of this Container.  # noqa: E501
        :type: ContainerConfig
        """

        self._config = config

    @property
    def active_graph_id(self):
        """Gets the active_graph_id of this Container.  # noqa: E501


        :return: The active_graph_id of this Container.  # noqa: E501
        :rtype: str
        """
        return self._active_graph_id

    @active_graph_id.setter
    def active_graph_id(self, active_graph_id):
        """Sets the active_graph_id of this Container.


        :param active_graph_id: The active_graph_id of this Container.  # noqa: E501
        :type: str
        """
        if active_graph_id is None:
            raise ValueError("Invalid value for `active_graph_id`, must not be `None`")  # noqa: E501

        self._active_graph_id = active_graph_id

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
        if issubclass(Container, dict):
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
        if not isinstance(other, Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
