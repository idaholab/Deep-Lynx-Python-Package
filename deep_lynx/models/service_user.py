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

class ServiceUser(object):
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
        'identity_provider': 'str',
        'display_name': 'str',
        'email': 'str',
        'admin': 'bool',
        'active': 'bool',
        'reset_required': 'bool',
        'email_valid': 'bool',
        'permissions': 'list[object]',
        'roles': 'list[object]',
        'id': 'str',
        'identity_provider_id': 'str',
        'created_at': 'str',
        'modified_at': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'reset_token_issued': 'str',
        'keys': 'list[ServiceUserKeys]'
    }

    attribute_map = {
        'identity_provider': 'identity_provider',
        'display_name': 'display_name',
        'email': 'email',
        'admin': 'admin',
        'active': 'active',
        'reset_required': 'reset_required',
        'email_valid': 'email_valid',
        'permissions': 'permissions',
        'roles': 'roles',
        'id': 'id',
        'identity_provider_id': 'identity_provider_id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'reset_token_issued': 'reset_token_issued',
        'keys': 'keys'
    }

    def __init__(self, identity_provider=None, display_name=None, email=None, admin=None, active=None, reset_required=None, email_valid=None, permissions=None, roles=None, id=None, identity_provider_id=None, created_at=None, modified_at=None, created_by=None, modified_by=None, reset_token_issued=None, keys=None):  # noqa: E501
        """ServiceUser - a model defined in Swagger"""  # noqa: E501
        self._identity_provider = None
        self._display_name = None
        self._email = None
        self._admin = None
        self._active = None
        self._reset_required = None
        self._email_valid = None
        self._permissions = None
        self._roles = None
        self._id = None
        self._identity_provider_id = None
        self._created_at = None
        self._modified_at = None
        self._created_by = None
        self._modified_by = None
        self._reset_token_issued = None
        self._keys = None
        self.discriminator = None
        self.identity_provider = identity_provider
        self.display_name = display_name
        self.email = email
        self.admin = admin
        self.active = active
        self.reset_required = reset_required
        self.email_valid = email_valid
        if permissions is not None:
            self.permissions = permissions
        if roles is not None:
            self.roles = roles
        self.id = id
        self.identity_provider_id = identity_provider_id
        self.created_at = created_at
        self.modified_at = modified_at
        self.created_by = created_by
        self.modified_by = modified_by
        self.reset_token_issued = reset_token_issued
        if keys is not None:
            self.keys = keys

    @property
    def identity_provider(self):
        """Gets the identity_provider of this ServiceUser.  # noqa: E501


        :return: The identity_provider of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this ServiceUser.


        :param identity_provider: The identity_provider of this ServiceUser.  # noqa: E501
        :type: str
        """
        if identity_provider is None:
            raise ValueError("Invalid value for `identity_provider`, must not be `None`")  # noqa: E501

        self._identity_provider = identity_provider

    @property
    def display_name(self):
        """Gets the display_name of this ServiceUser.  # noqa: E501


        :return: The display_name of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServiceUser.


        :param display_name: The display_name of this ServiceUser.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this ServiceUser.  # noqa: E501


        :return: The email of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ServiceUser.


        :param email: The email of this ServiceUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def admin(self):
        """Gets the admin of this ServiceUser.  # noqa: E501


        :return: The admin of this ServiceUser.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this ServiceUser.


        :param admin: The admin of this ServiceUser.  # noqa: E501
        :type: bool
        """
        if admin is None:
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def active(self):
        """Gets the active of this ServiceUser.  # noqa: E501


        :return: The active of this ServiceUser.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ServiceUser.


        :param active: The active of this ServiceUser.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def reset_required(self):
        """Gets the reset_required of this ServiceUser.  # noqa: E501


        :return: The reset_required of this ServiceUser.  # noqa: E501
        :rtype: bool
        """
        return self._reset_required

    @reset_required.setter
    def reset_required(self, reset_required):
        """Sets the reset_required of this ServiceUser.


        :param reset_required: The reset_required of this ServiceUser.  # noqa: E501
        :type: bool
        """
        if reset_required is None:
            raise ValueError("Invalid value for `reset_required`, must not be `None`")  # noqa: E501

        self._reset_required = reset_required

    @property
    def email_valid(self):
        """Gets the email_valid of this ServiceUser.  # noqa: E501


        :return: The email_valid of this ServiceUser.  # noqa: E501
        :rtype: bool
        """
        return self._email_valid

    @email_valid.setter
    def email_valid(self, email_valid):
        """Sets the email_valid of this ServiceUser.


        :param email_valid: The email_valid of this ServiceUser.  # noqa: E501
        :type: bool
        """
        if email_valid is None:
            raise ValueError("Invalid value for `email_valid`, must not be `None`")  # noqa: E501

        self._email_valid = email_valid

    @property
    def permissions(self):
        """Gets the permissions of this ServiceUser.  # noqa: E501


        :return: The permissions of this ServiceUser.  # noqa: E501
        :rtype: list[object]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ServiceUser.


        :param permissions: The permissions of this ServiceUser.  # noqa: E501
        :type: list[object]
        """

        self._permissions = permissions

    @property
    def roles(self):
        """Gets the roles of this ServiceUser.  # noqa: E501


        :return: The roles of this ServiceUser.  # noqa: E501
        :rtype: list[object]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ServiceUser.


        :param roles: The roles of this ServiceUser.  # noqa: E501
        :type: list[object]
        """

        self._roles = roles

    @property
    def id(self):
        """Gets the id of this ServiceUser.  # noqa: E501


        :return: The id of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceUser.


        :param id: The id of this ServiceUser.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def identity_provider_id(self):
        """Gets the identity_provider_id of this ServiceUser.  # noqa: E501


        :return: The identity_provider_id of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._identity_provider_id

    @identity_provider_id.setter
    def identity_provider_id(self, identity_provider_id):
        """Sets the identity_provider_id of this ServiceUser.


        :param identity_provider_id: The identity_provider_id of this ServiceUser.  # noqa: E501
        :type: str
        """
        if identity_provider_id is None:
            raise ValueError("Invalid value for `identity_provider_id`, must not be `None`")  # noqa: E501

        self._identity_provider_id = identity_provider_id

    @property
    def created_at(self):
        """Gets the created_at of this ServiceUser.  # noqa: E501


        :return: The created_at of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ServiceUser.


        :param created_at: The created_at of this ServiceUser.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this ServiceUser.  # noqa: E501


        :return: The modified_at of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ServiceUser.


        :param modified_at: The modified_at of this ServiceUser.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this ServiceUser.  # noqa: E501


        :return: The created_by of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ServiceUser.


        :param created_by: The created_by of this ServiceUser.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this ServiceUser.  # noqa: E501


        :return: The modified_by of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this ServiceUser.


        :param modified_by: The modified_by of this ServiceUser.  # noqa: E501
        :type: str
        """
        if modified_by is None:
            raise ValueError("Invalid value for `modified_by`, must not be `None`")  # noqa: E501

        self._modified_by = modified_by

    @property
    def reset_token_issued(self):
        """Gets the reset_token_issued of this ServiceUser.  # noqa: E501


        :return: The reset_token_issued of this ServiceUser.  # noqa: E501
        :rtype: str
        """
        return self._reset_token_issued

    @reset_token_issued.setter
    def reset_token_issued(self, reset_token_issued):
        """Sets the reset_token_issued of this ServiceUser.


        :param reset_token_issued: The reset_token_issued of this ServiceUser.  # noqa: E501
        :type: str
        """
        if reset_token_issued is None:
            raise ValueError("Invalid value for `reset_token_issued`, must not be `None`")  # noqa: E501

        self._reset_token_issued = reset_token_issued

    @property
    def keys(self):
        """Gets the keys of this ServiceUser.  # noqa: E501


        :return: The keys of this ServiceUser.  # noqa: E501
        :rtype: list[ServiceUserKeys]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ServiceUser.


        :param keys: The keys of this ServiceUser.  # noqa: E501
        :type: list[ServiceUserKeys]
        """

        self._keys = keys

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
        if issubclass(ServiceUser, dict):
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
        if not isinstance(other, ServiceUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
