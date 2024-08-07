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

class RelationshipPair(object):
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
        'relationship_type': 'str',
        'relationship_id': 'str',
        'origin_metatype_id': 'str',
        'destination_metatype_id': 'str',
        'id': 'str',
        'archived': 'bool',
        'container_id': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'origin_metatype_name': 'str',
        'destination_metatype_name': 'str',
        'relationship_pair_name': 'str',
        'destination_metatype': 'RelationshipPairDestinationMetatype',
        'origin_metatype': 'RelationshipPairDestinationMetatype',
        'relationship': 'RelationshipPairDestinationMetatype'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'relationship_type': 'relationship_type',
        'relationship_id': 'relationship_id',
        'origin_metatype_id': 'origin_metatype_id',
        'destination_metatype_id': 'destination_metatype_id',
        'id': 'id',
        'archived': 'archived',
        'container_id': 'container_id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'origin_metatype_name': 'origin_metatype_name',
        'destination_metatype_name': 'destination_metatype_name',
        'relationship_pair_name': 'relationship_pair_name',
        'destination_metatype': 'destination_metatype',
        'origin_metatype': 'origin_metatype',
        'relationship': 'relationship'
    }

    def __init__(self, name=None, description=None, relationship_type=None, relationship_id=None, origin_metatype_id=None, destination_metatype_id=None, id=None, archived=None, container_id=None, created_at=None, modified_at=None, created_by=None, modified_by=None, origin_metatype_name=None, destination_metatype_name=None, relationship_pair_name=None, destination_metatype=None, origin_metatype=None, relationship=None):  # noqa: E501
        """RelationshipPair - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._relationship_type = None
        self._relationship_id = None
        self._origin_metatype_id = None
        self._destination_metatype_id = None
        self._id = None
        self._archived = None
        self._container_id = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._origin_metatype_name = None
        self._destination_metatype_name = None
        self._relationship_pair_name = None
        self._destination_metatype = None
        self._origin_metatype = None
        self._relationship = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if relationship_type is not None:
            self.relationship_type = relationship_type
        if relationship_id is not None:
            self.relationship_id = relationship_id
        if origin_metatype_id is not None:
            self.origin_metatype_id = origin_metatype_id
        if destination_metatype_id is not None:
            self.destination_metatype_id = destination_metatype_id
        self.id = id
        if archived is not None:
            self.archived = archived
        if container_id is not None:
            self.container_id = container_id
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if origin_metatype_name is not None:
            self.origin_metatype_name = origin_metatype_name
        if destination_metatype_name is not None:
            self.destination_metatype_name = destination_metatype_name
        if relationship_pair_name is not None:
            self.relationship_pair_name = relationship_pair_name
        if destination_metatype is not None:
            self.destination_metatype = destination_metatype
        if origin_metatype is not None:
            self.origin_metatype = origin_metatype
        if relationship is not None:
            self.relationship = relationship

    @property
    def name(self):
        """Gets the name of this RelationshipPair.  # noqa: E501


        :return: The name of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelationshipPair.


        :param name: The name of this RelationshipPair.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RelationshipPair.  # noqa: E501


        :return: The description of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RelationshipPair.


        :param description: The description of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def relationship_type(self):
        """Gets the relationship_type of this RelationshipPair.  # noqa: E501


        :return: The relationship_type of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """Sets the relationship_type of this RelationshipPair.


        :param relationship_type: The relationship_type of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._relationship_type = relationship_type

    @property
    def relationship_id(self):
        """Gets the relationship_id of this RelationshipPair.  # noqa: E501


        :return: The relationship_id of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._relationship_id

    @relationship_id.setter
    def relationship_id(self, relationship_id):
        """Sets the relationship_id of this RelationshipPair.


        :param relationship_id: The relationship_id of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._relationship_id = relationship_id

    @property
    def origin_metatype_id(self):
        """Gets the origin_metatype_id of this RelationshipPair.  # noqa: E501


        :return: The origin_metatype_id of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._origin_metatype_id

    @origin_metatype_id.setter
    def origin_metatype_id(self, origin_metatype_id):
        """Sets the origin_metatype_id of this RelationshipPair.


        :param origin_metatype_id: The origin_metatype_id of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._origin_metatype_id = origin_metatype_id

    @property
    def destination_metatype_id(self):
        """Gets the destination_metatype_id of this RelationshipPair.  # noqa: E501


        :return: The destination_metatype_id of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._destination_metatype_id

    @destination_metatype_id.setter
    def destination_metatype_id(self, destination_metatype_id):
        """Sets the destination_metatype_id of this RelationshipPair.


        :param destination_metatype_id: The destination_metatype_id of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._destination_metatype_id = destination_metatype_id

    @property
    def id(self):
        """Gets the id of this RelationshipPair.  # noqa: E501


        :return: The id of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationshipPair.


        :param id: The id of this RelationshipPair.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def archived(self):
        """Gets the archived of this RelationshipPair.  # noqa: E501


        :return: The archived of this RelationshipPair.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this RelationshipPair.


        :param archived: The archived of this RelationshipPair.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def container_id(self):
        """Gets the container_id of this RelationshipPair.  # noqa: E501


        :return: The container_id of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this RelationshipPair.


        :param container_id: The container_id of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def created_at(self):
        """Gets the created_at of this RelationshipPair.  # noqa: E501


        :return: The created_at of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RelationshipPair.


        :param created_at: The created_at of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this RelationshipPair.  # noqa: E501


        :return: The modified_at of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this RelationshipPair.


        :param modified_at: The modified_at of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this RelationshipPair.  # noqa: E501


        :return: The created_by of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RelationshipPair.


        :param created_by: The created_by of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this RelationshipPair.  # noqa: E501


        :return: The modified_by of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this RelationshipPair.


        :param modified_by: The modified_by of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def origin_metatype_name(self):
        """Gets the origin_metatype_name of this RelationshipPair.  # noqa: E501


        :return: The origin_metatype_name of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._origin_metatype_name

    @origin_metatype_name.setter
    def origin_metatype_name(self, origin_metatype_name):
        """Sets the origin_metatype_name of this RelationshipPair.


        :param origin_metatype_name: The origin_metatype_name of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._origin_metatype_name = origin_metatype_name

    @property
    def destination_metatype_name(self):
        """Gets the destination_metatype_name of this RelationshipPair.  # noqa: E501


        :return: The destination_metatype_name of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._destination_metatype_name

    @destination_metatype_name.setter
    def destination_metatype_name(self, destination_metatype_name):
        """Sets the destination_metatype_name of this RelationshipPair.


        :param destination_metatype_name: The destination_metatype_name of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._destination_metatype_name = destination_metatype_name

    @property
    def relationship_pair_name(self):
        """Gets the relationship_pair_name of this RelationshipPair.  # noqa: E501


        :return: The relationship_pair_name of this RelationshipPair.  # noqa: E501
        :rtype: str
        """
        return self._relationship_pair_name

    @relationship_pair_name.setter
    def relationship_pair_name(self, relationship_pair_name):
        """Sets the relationship_pair_name of this RelationshipPair.


        :param relationship_pair_name: The relationship_pair_name of this RelationshipPair.  # noqa: E501
        :type: str
        """

        self._relationship_pair_name = relationship_pair_name

    @property
    def destination_metatype(self):
        """Gets the destination_metatype of this RelationshipPair.  # noqa: E501


        :return: The destination_metatype of this RelationshipPair.  # noqa: E501
        :rtype: RelationshipPairDestinationMetatype
        """
        return self._destination_metatype

    @destination_metatype.setter
    def destination_metatype(self, destination_metatype):
        """Sets the destination_metatype of this RelationshipPair.


        :param destination_metatype: The destination_metatype of this RelationshipPair.  # noqa: E501
        :type: RelationshipPairDestinationMetatype
        """

        self._destination_metatype = destination_metatype

    @property
    def origin_metatype(self):
        """Gets the origin_metatype of this RelationshipPair.  # noqa: E501


        :return: The origin_metatype of this RelationshipPair.  # noqa: E501
        :rtype: RelationshipPairDestinationMetatype
        """
        return self._origin_metatype

    @origin_metatype.setter
    def origin_metatype(self, origin_metatype):
        """Sets the origin_metatype of this RelationshipPair.


        :param origin_metatype: The origin_metatype of this RelationshipPair.  # noqa: E501
        :type: RelationshipPairDestinationMetatype
        """

        self._origin_metatype = origin_metatype

    @property
    def relationship(self):
        """Gets the relationship of this RelationshipPair.  # noqa: E501


        :return: The relationship of this RelationshipPair.  # noqa: E501
        :rtype: RelationshipPairDestinationMetatype
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this RelationshipPair.


        :param relationship: The relationship of this RelationshipPair.  # noqa: E501
        :type: RelationshipPairDestinationMetatype
        """

        self._relationship = relationship

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
        if issubclass(RelationshipPair, dict):
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
        if not isinstance(other, RelationshipPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
