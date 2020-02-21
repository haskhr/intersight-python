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


class IaasConnectorPack(object):
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
        'complete_version': 'str',
        'dependency_names': 'list[str]',
        'downloaded_version': 'str',
        'name': 'str',
        'state': 'str',
        'version': 'str',
        'guid': 'IaasUcsdInfoRef'
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
        'complete_version': 'CompleteVersion',
        'dependency_names': 'DependencyNames',
        'downloaded_version': 'DownloadedVersion',
        'name': 'Name',
        'state': 'State',
        'version': 'Version',
        'guid': 'Guid'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, complete_version=None, dependency_names=None, downloaded_version=None, name=None, state=None, version=None, guid=None):
        """
        IaasConnectorPack - a model defined in Swagger
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
        self._complete_version = None
        self._dependency_names = None
        self._downloaded_version = None
        self._name = None
        self._state = None
        self._version = None
        self._guid = None

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
        if complete_version is not None:
          self.complete_version = complete_version
        if dependency_names is not None:
          self.dependency_names = dependency_names
        if downloaded_version is not None:
          self.downloaded_version = downloaded_version
        if name is not None:
          self.name = name
        if state is not None:
          self.state = state
        if version is not None:
          self.version = version
        if guid is not None:
          self.guid = guid

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IaasConnectorPack.
        The Account ID for this managed object.  

        :return: The account_moid of this IaasConnectorPack.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IaasConnectorPack.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IaasConnectorPack.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this IaasConnectorPack.
        The time when this managed object was created.  

        :return: The create_time of this IaasConnectorPack.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IaasConnectorPack.
        The time when this managed object was created.  

        :param create_time: The create_time of this IaasConnectorPack.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IaasConnectorPack.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IaasConnectorPack.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IaasConnectorPack.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IaasConnectorPack.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IaasConnectorPack.
        The time when this managed object was last modified.  

        :return: The mod_time of this IaasConnectorPack.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IaasConnectorPack.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IaasConnectorPack.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IaasConnectorPack.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this IaasConnectorPack.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IaasConnectorPack.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this IaasConnectorPack.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IaasConnectorPack.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this IaasConnectorPack.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IaasConnectorPack.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this IaasConnectorPack.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IaasConnectorPack.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IaasConnectorPack.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IaasConnectorPack.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IaasConnectorPack.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IaasConnectorPack.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IaasConnectorPack.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IaasConnectorPack.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IaasConnectorPack.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IaasConnectorPack.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IaasConnectorPack.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IaasConnectorPack.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IaasConnectorPack.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IaasConnectorPack.
        The versioning info for this managed object.   

        :return: The version_context of this IaasConnectorPack.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IaasConnectorPack.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IaasConnectorPack.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IaasConnectorPack.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IaasConnectorPack.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IaasConnectorPack.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IaasConnectorPack.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this IaasConnectorPack.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IaasConnectorPack.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IaasConnectorPack.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IaasConnectorPack.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this IaasConnectorPack.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this IaasConnectorPack.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this IaasConnectorPack.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this IaasConnectorPack.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def complete_version(self):
        """
        Gets the complete_version of this IaasConnectorPack.
        Complete version of the connector pack including build number.  

        :return: The complete_version of this IaasConnectorPack.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        """
        Sets the complete_version of this IaasConnectorPack.
        Complete version of the connector pack including build number.  

        :param complete_version: The complete_version of this IaasConnectorPack.
        :type: str
        """

        self._complete_version = complete_version

    @property
    def dependency_names(self):
        """
        Gets the dependency_names of this IaasConnectorPack.
        List of dependent connectors on the UCSD for this connector. For example BigData depends on UCS Connector.  

        :return: The dependency_names of this IaasConnectorPack.
        :rtype: list[str]
        """
        return self._dependency_names

    @dependency_names.setter
    def dependency_names(self, dependency_names):
        """
        Sets the dependency_names of this IaasConnectorPack.
        List of dependent connectors on the UCSD for this connector. For example BigData depends on UCS Connector.  

        :param dependency_names: The dependency_names of this IaasConnectorPack.
        :type: list[str]
        """

        self._dependency_names = dependency_names

    @property
    def downloaded_version(self):
        """
        Gets the downloaded_version of this IaasConnectorPack.
        Version of the connector pack that is last downloaded successfully to UCSD.  

        :return: The downloaded_version of this IaasConnectorPack.
        :rtype: str
        """
        return self._downloaded_version

    @downloaded_version.setter
    def downloaded_version(self, downloaded_version):
        """
        Sets the downloaded_version of this IaasConnectorPack.
        Version of the connector pack that is last downloaded successfully to UCSD.  

        :param downloaded_version: The downloaded_version of this IaasConnectorPack.
        :type: str
        """

        self._downloaded_version = downloaded_version

    @property
    def name(self):
        """
        Gets the name of this IaasConnectorPack.
        Name of the connector pack running on the UCSD.  

        :return: The name of this IaasConnectorPack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IaasConnectorPack.
        Name of the connector pack running on the UCSD.  

        :param name: The name of this IaasConnectorPack.
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """
        Gets the state of this IaasConnectorPack.
        State of the connector pack whether it is enabled or disabled.  

        :return: The state of this IaasConnectorPack.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this IaasConnectorPack.
        State of the connector pack whether it is enabled or disabled.  

        :param state: The state of this IaasConnectorPack.
        :type: str
        """

        self._state = state

    @property
    def version(self):
        """
        Gets the version of this IaasConnectorPack.
        Version of the connector pack.   

        :return: The version of this IaasConnectorPack.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this IaasConnectorPack.
        Version of the connector pack.   

        :param version: The version of this IaasConnectorPack.
        :type: str
        """

        self._version = version

    @property
    def guid(self):
        """
        Gets the guid of this IaasConnectorPack.
        A collection of references to the [iaas.UcsdInfo](mo://iaas.UcsdInfo) Managed Object.  When this managed object is deleted, the referenced [iaas.UcsdInfo](mo://iaas.UcsdInfo) MO unsets its reference to this deleted MO. 

        :return: The guid of this IaasConnectorPack.
        :rtype: IaasUcsdInfoRef
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this IaasConnectorPack.
        A collection of references to the [iaas.UcsdInfo](mo://iaas.UcsdInfo) Managed Object.  When this managed object is deleted, the referenced [iaas.UcsdInfo](mo://iaas.UcsdInfo) MO unsets its reference to this deleted MO. 

        :param guid: The guid of this IaasConnectorPack.
        :type: IaasUcsdInfoRef
        """

        self._guid = guid

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
        if not isinstance(other, IaasConnectorPack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
