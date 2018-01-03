# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IamEndPointUserRole(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'account_moid': 'str',
        'ancestors': 'list[MoMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoMoRef',
        'tags': 'list[MoTag]',
        'enabled': 'bool',
        'end_point_role': 'MoMoRef',
        'end_point_user': 'MoMoRef',
        'end_point_user_policy': 'MoMoRef',
        'password': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'enabled': 'Enabled',
        'end_point_role': 'EndPointRole',
        'end_point_user': 'EndPointUser',
        'end_point_user_policy': 'EndPointUserPolicy',
        'password': 'Password'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, enabled=None, end_point_role=None, end_point_user=None, end_point_user_policy=None, password=None):
        """
        IamEndPointUserRole - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._enabled = None
        self._end_point_role = None
        self._end_point_user = None
        self._end_point_user_policy = None
        self._password = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if enabled is not None:
          self.enabled = enabled
        if end_point_role is not None:
          self.end_point_role = end_point_role
        if end_point_user is not None:
          self.end_point_user = end_point_user
        if end_point_user_policy is not None:
          self.end_point_user_policy = end_point_user_policy
        if password is not None:
          self.password = password

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamEndPointUserRole.
        The Account ID for this managed object.  

        :return: The account_moid of this IamEndPointUserRole.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamEndPointUserRole.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamEndPointUserRole.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamEndPointUserRole.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamEndPointUserRole.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamEndPointUserRole.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamEndPointUserRole.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamEndPointUserRole.
        The time when this managed object was created.  

        :return: The create_time of this IamEndPointUserRole.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamEndPointUserRole.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamEndPointUserRole.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamEndPointUserRole.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamEndPointUserRole.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamEndPointUserRole.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamEndPointUserRole.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamEndPointUserRole.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamEndPointUserRole.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamEndPointUserRole.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamEndPointUserRole.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamEndPointUserRole.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamEndPointUserRole.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamEndPointUserRole.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamEndPointUserRole.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamEndPointUserRole.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamEndPointUserRole.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamEndPointUserRole.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamEndPointUserRole.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamEndPointUserRole.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamEndPointUserRole.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamEndPointUserRole.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamEndPointUserRole.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamEndPointUserRole.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IamEndPointUserRole.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamEndPointUserRole.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IamEndPointUserRole.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def enabled(self):
        """
        Gets the enabled of this IamEndPointUserRole.
        Enables the user account on the endpoint  

        :return: The enabled of this IamEndPointUserRole.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this IamEndPointUserRole.
        Enables the user account on the endpoint  

        :param enabled: The enabled of this IamEndPointUserRole.
        :type: bool
        """

        self._enabled = enabled

    @property
    def end_point_role(self):
        """
        Gets the end_point_role of this IamEndPointUserRole.
        Relationship to the Endpoint role 

        :return: The end_point_role of this IamEndPointUserRole.
        :rtype: MoMoRef
        """
        return self._end_point_role

    @end_point_role.setter
    def end_point_role(self, end_point_role):
        """
        Sets the end_point_role of this IamEndPointUserRole.
        Relationship to the Endpoint role 

        :param end_point_role: The end_point_role of this IamEndPointUserRole.
        :type: MoMoRef
        """

        self._end_point_role = end_point_role

    @property
    def end_point_user(self):
        """
        Gets the end_point_user of this IamEndPointUserRole.
        Relationship to the Endpoint user 

        :return: The end_point_user of this IamEndPointUserRole.
        :rtype: MoMoRef
        """
        return self._end_point_user

    @end_point_user.setter
    def end_point_user(self, end_point_user):
        """
        Sets the end_point_user of this IamEndPointUserRole.
        Relationship to the Endpoint user 

        :param end_point_user: The end_point_user of this IamEndPointUserRole.
        :type: MoMoRef
        """

        self._end_point_user = end_point_user

    @property
    def end_point_user_policy(self):
        """
        Gets the end_point_user_policy of this IamEndPointUserRole.

        :return: The end_point_user_policy of this IamEndPointUserRole.
        :rtype: MoMoRef
        """
        return self._end_point_user_policy

    @end_point_user_policy.setter
    def end_point_user_policy(self, end_point_user_policy):
        """
        Sets the end_point_user_policy of this IamEndPointUserRole.

        :param end_point_user_policy: The end_point_user_policy of this IamEndPointUserRole.
        :type: MoMoRef
        """

        self._end_point_user_policy = end_point_user_policy

    @property
    def password(self):
        """
        Gets the password of this IamEndPointUserRole.
        Password for the endpoint user   

        :return: The password of this IamEndPointUserRole.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this IamEndPointUserRole.
        Password for the endpoint user   

        :param password: The password of this IamEndPointUserRole.
        :type: str
        """

        self._password = password

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IamEndPointUserRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
