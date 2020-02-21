# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1415
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IamAccount(object):
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
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoOptionalTag]',
        'version_context': 'MoOptionalVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'name': 'str',
        'status': 'str',
        '_0_encrypt': 'CryptEncryptRef',
        '_1_decrypt': 'CryptDecryptRef',
        'app_registrations': 'list[IamAppRegistrationRef]',
        'domain_groups': 'list[IamDomainGroupRef]',
        'end_point_roles': 'list[IamEndPointRoleRef]',
        'idpreferences': 'list[IamIdpReferenceRef]',
        'idps': 'list[IamIdpRef]',
        'permissions': 'list[IamPermissionRef]',
        'privilege_sets': 'list[IamPrivilegeSetRef]',
        'privileges': 'list[IamPrivilegeRef]',
        'resource_limits': 'IamResourceLimitsRef',
        'roles': 'list[IamRoleRef]',
        'security_holder': 'IamSecurityHolderRef',
        'session_limits': 'IamSessionLimitsRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'name': 'Name',
        'status': 'Status',
        '_0_encrypt': '_0_Encrypt',
        '_1_decrypt': '_1_Decrypt',
        'app_registrations': 'AppRegistrations',
        'domain_groups': 'DomainGroups',
        'end_point_roles': 'EndPointRoles',
        'idpreferences': 'Idpreferences',
        'idps': 'Idps',
        'permissions': 'Permissions',
        'privilege_sets': 'PrivilegeSets',
        'privileges': 'Privileges',
        'resource_limits': 'ResourceLimits',
        'roles': 'Roles',
        'security_holder': 'SecurityHolder',
        'session_limits': 'SessionLimits'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, name=None, status=None, _0_encrypt=None, _1_decrypt=None, app_registrations=None, domain_groups=None, end_point_roles=None, idpreferences=None, idps=None, permissions=None, privilege_sets=None, privileges=None, resource_limits=None, roles=None, security_holder=None, session_limits=None):
        """
        IamAccount - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._name = None
        self._status = None
        self.__0_encrypt = None
        self.__1_decrypt = None
        self._app_registrations = None
        self._domain_groups = None
        self._end_point_roles = None
        self._idpreferences = None
        self._idps = None
        self._permissions = None
        self._privilege_sets = None
        self._privileges = None
        self._resource_limits = None
        self._roles = None
        self._security_holder = None
        self._session_limits = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if _0_encrypt is not None:
          self._0_encrypt = _0_encrypt
        if _1_decrypt is not None:
          self._1_decrypt = _1_decrypt
        if app_registrations is not None:
          self.app_registrations = app_registrations
        if domain_groups is not None:
          self.domain_groups = domain_groups
        if end_point_roles is not None:
          self.end_point_roles = end_point_roles
        if idpreferences is not None:
          self.idpreferences = idpreferences
        if idps is not None:
          self.idps = idps
        if permissions is not None:
          self.permissions = permissions
        if privilege_sets is not None:
          self.privilege_sets = privilege_sets
        if privileges is not None:
          self.privileges = privileges
        if resource_limits is not None:
          self.resource_limits = resource_limits
        if roles is not None:
          self.roles = roles
        if security_holder is not None:
          self.security_holder = security_holder
        if session_limits is not None:
          self.session_limits = session_limits

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamAccount.
        The Account ID for this managed object.  

        :return: The account_moid of this IamAccount.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamAccount.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamAccount.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this IamAccount.
        The time when this managed object was created.  

        :return: The create_time of this IamAccount.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamAccount.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamAccount.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamAccount.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamAccount.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamAccount.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamAccount.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamAccount.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamAccount.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamAccount.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamAccount.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamAccount.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this IamAccount.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamAccount.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this IamAccount.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamAccount.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this IamAccount.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamAccount.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this IamAccount.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamAccount.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamAccount.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamAccount.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamAccount.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamAccount.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamAccount.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamAccount.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamAccount.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamAccount.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IamAccount.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamAccount.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IamAccount.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamAccount.
        The versioning info for this managed object.   

        :return: The version_context of this IamAccount.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamAccount.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamAccount.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamAccount.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamAccount.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamAccount.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamAccount.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this IamAccount.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamAccount.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamAccount.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamAccount.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this IamAccount.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this IamAccount.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this IamAccount.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this IamAccount.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def name(self):
        """
        Gets the name of this IamAccount.
        Name of the Intersight account. By default, name is same as the MoID of the account.  

        :return: The name of this IamAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamAccount.
        Name of the Intersight account. By default, name is same as the MoID of the account.  

        :param name: The name of this IamAccount.
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this IamAccount.
        Status of the account. To activate the Intersight account, claim a device to the account.   

        :return: The status of this IamAccount.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this IamAccount.
        Status of the account. To activate the Intersight account, claim a device to the account.   

        :param status: The status of this IamAccount.
        :type: str
        """

        self._status = status

    @property
    def _0_encrypt(self):
        """
        Gets the _0_encrypt of this IamAccount.
        A collection of references to the [crypt.Encrypt](mo://crypt.Encrypt) Managed Object.  When this managed object is deleted, the referenced [crypt.Encrypt](mo://crypt.Encrypt) MO unsets its reference to this deleted MO. 

        :return: The _0_encrypt of this IamAccount.
        :rtype: CryptEncryptRef
        """
        return self.__0_encrypt

    @_0_encrypt.setter
    def _0_encrypt(self, _0_encrypt):
        """
        Sets the _0_encrypt of this IamAccount.
        A collection of references to the [crypt.Encrypt](mo://crypt.Encrypt) Managed Object.  When this managed object is deleted, the referenced [crypt.Encrypt](mo://crypt.Encrypt) MO unsets its reference to this deleted MO. 

        :param _0_encrypt: The _0_encrypt of this IamAccount.
        :type: CryptEncryptRef
        """

        self.__0_encrypt = _0_encrypt

    @property
    def _1_decrypt(self):
        """
        Gets the _1_decrypt of this IamAccount.
        A collection of references to the [crypt.Decrypt](mo://crypt.Decrypt) Managed Object.  When this managed object is deleted, the referenced [crypt.Decrypt](mo://crypt.Decrypt) MO unsets its reference to this deleted MO. 

        :return: The _1_decrypt of this IamAccount.
        :rtype: CryptDecryptRef
        """
        return self.__1_decrypt

    @_1_decrypt.setter
    def _1_decrypt(self, _1_decrypt):
        """
        Sets the _1_decrypt of this IamAccount.
        A collection of references to the [crypt.Decrypt](mo://crypt.Decrypt) Managed Object.  When this managed object is deleted, the referenced [crypt.Decrypt](mo://crypt.Decrypt) MO unsets its reference to this deleted MO. 

        :param _1_decrypt: The _1_decrypt of this IamAccount.
        :type: CryptDecryptRef
        """

        self.__1_decrypt = _1_decrypt

    @property
    def app_registrations(self):
        """
        Gets the app_registrations of this IamAccount.
        List of registered OAuth2 applications created from the account. 

        :return: The app_registrations of this IamAccount.
        :rtype: list[IamAppRegistrationRef]
        """
        return self._app_registrations

    @app_registrations.setter
    def app_registrations(self, app_registrations):
        """
        Sets the app_registrations of this IamAccount.
        List of registered OAuth2 applications created from the account. 

        :param app_registrations: The app_registrations of this IamAccount.
        :type: list[IamAppRegistrationRef]
        """

        self._app_registrations = app_registrations

    @property
    def domain_groups(self):
        """
        Gets the domain_groups of this IamAccount.
        The domain Groups are configured in an account for scaling purpose. Currently, only onboarding-device account has multiple domain groups and other accounts have only one domain group per account. 

        :return: The domain_groups of this IamAccount.
        :rtype: list[IamDomainGroupRef]
        """
        return self._domain_groups

    @domain_groups.setter
    def domain_groups(self, domain_groups):
        """
        Sets the domain_groups of this IamAccount.
        The domain Groups are configured in an account for scaling purpose. Currently, only onboarding-device account has multiple domain groups and other accounts have only one domain group per account. 

        :param domain_groups: The domain_groups of this IamAccount.
        :type: list[IamDomainGroupRef]
        """

        self._domain_groups = domain_groups

    @property
    def end_point_roles(self):
        """
        Gets the end_point_roles of this IamAccount.
        User defined end point roles. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch. 

        :return: The end_point_roles of this IamAccount.
        :rtype: list[IamEndPointRoleRef]
        """
        return self._end_point_roles

    @end_point_roles.setter
    def end_point_roles(self, end_point_roles):
        """
        Sets the end_point_roles of this IamAccount.
        User defined end point roles. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch. 

        :param end_point_roles: The end_point_roles of this IamAccount.
        :type: list[IamEndPointRoleRef]
        """

        self._end_point_roles = end_point_roles

    @property
    def idpreferences(self):
        """
        Gets the idpreferences of this IamAccount.
        System created IdPs configured for authentication in an account. By default Cisco IdP is created upon account creation. 

        :return: The idpreferences of this IamAccount.
        :rtype: list[IamIdpReferenceRef]
        """
        return self._idpreferences

    @idpreferences.setter
    def idpreferences(self, idpreferences):
        """
        Sets the idpreferences of this IamAccount.
        System created IdPs configured for authentication in an account. By default Cisco IdP is created upon account creation. 

        :param idpreferences: The idpreferences of this IamAccount.
        :type: list[IamIdpReferenceRef]
        """

        self._idpreferences = idpreferences

    @property
    def idps(self):
        """
        Gets the idps of this IamAccount.
        IdPs configured for authentication in an account. IdP object handles the third-party IdP details. 

        :return: The idps of this IamAccount.
        :rtype: list[IamIdpRef]
        """
        return self._idps

    @idps.setter
    def idps(self, idps):
        """
        Sets the idps of this IamAccount.
        IdPs configured for authentication in an account. IdP object handles the third-party IdP details. 

        :param idps: The idps of this IamAccount.
        :type: list[IamIdpRef]
        """

        self._idps = idps

    @property
    def permissions(self):
        """
        Gets the permissions of this IamAccount.
        System defined permissions within an account. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :return: The permissions of this IamAccount.
        :rtype: list[IamPermissionRef]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this IamAccount.
        System defined permissions within an account. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :param permissions: The permissions of this IamAccount.
        :type: list[IamPermissionRef]
        """

        self._permissions = permissions

    @property
    def privilege_sets(self):
        """
        Gets the privilege_sets of this IamAccount.
        User defined privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles. 

        :return: The privilege_sets of this IamAccount.
        :rtype: list[IamPrivilegeSetRef]
        """
        return self._privilege_sets

    @privilege_sets.setter
    def privilege_sets(self, privilege_sets):
        """
        Sets the privilege_sets of this IamAccount.
        User defined privilege sets. Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles. 

        :param privilege_sets: The privilege_sets of this IamAccount.
        :type: list[IamPrivilegeSetRef]
        """

        self._privilege_sets = privilege_sets

    @property
    def privileges(self):
        """
        Gets the privileges of this IamAccount.
        Privileges are assigned to a user using privilege sets and roles. Privileges define user permissions and the actions a user can perform in Intersight. 

        :return: The privileges of this IamAccount.
        :rtype: list[IamPrivilegeRef]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """
        Sets the privileges of this IamAccount.
        Privileges are assigned to a user using privilege sets and roles. Privileges define user permissions and the actions a user can perform in Intersight. 

        :param privileges: The privileges of this IamAccount.
        :type: list[IamPrivilegeRef]
        """

        self._privileges = privileges

    @property
    def resource_limits(self):
        """
        Gets the resource_limits of this IamAccount.
        User and user group related configuration limits. 

        :return: The resource_limits of this IamAccount.
        :rtype: IamResourceLimitsRef
        """
        return self._resource_limits

    @resource_limits.setter
    def resource_limits(self, resource_limits):
        """
        Sets the resource_limits of this IamAccount.
        User and user group related configuration limits. 

        :param resource_limits: The resource_limits of this IamAccount.
        :type: IamResourceLimitsRef
        """

        self._resource_limits = resource_limits

    @property
    def roles(self):
        """
        Gets the roles of this IamAccount.
        User defined roles created within an account. Role is a collection of privilege sets. Roles are assigned to user using permission object. 

        :return: The roles of this IamAccount.
        :rtype: list[IamRoleRef]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this IamAccount.
        User defined roles created within an account. Role is a collection of privilege sets. Roles are assigned to user using permission object. 

        :param roles: The roles of this IamAccount.
        :type: list[IamRoleRef]
        """

        self._roles = roles

    @property
    def security_holder(self):
        """
        Gets the security_holder of this IamAccount.
        Holder for organization aggregated permissions and global account permissions. 

        :return: The security_holder of this IamAccount.
        :rtype: IamSecurityHolderRef
        """
        return self._security_holder

    @security_holder.setter
    def security_holder(self, security_holder):
        """
        Sets the security_holder of this IamAccount.
        Holder for organization aggregated permissions and global account permissions. 

        :param security_holder: The security_holder of this IamAccount.
        :type: IamSecurityHolderRef
        """

        self._security_holder = security_holder

    @property
    def session_limits(self):
        """
        Gets the session_limits of this IamAccount.
        Session related configuration limits. 

        :return: The session_limits of this IamAccount.
        :rtype: IamSessionLimitsRef
        """
        return self._session_limits

    @session_limits.setter
    def session_limits(self, session_limits):
        """
        Sets the session_limits of this IamAccount.
        Session related configuration limits. 

        :param session_limits: The session_limits of this IamAccount.
        :type: IamSessionLimitsRef
        """

        self._session_limits = session_limits

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
        if not isinstance(other, IamAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
