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


class StoragePhysicalPort(object):
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
        'iqn': 'str',
        'name': 'str',
        'speed': 'int',
        'status': 'str',
        'type': 'str',
        'wwn': 'str',
        'wwnn': 'str',
        'wwpn': 'str',
        'controller': 'StorageArrayControllerRef',
        'storage_array': 'StorageGenericArrayRef'
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
        'iqn': 'Iqn',
        'name': 'Name',
        'speed': 'Speed',
        'status': 'Status',
        'type': 'Type',
        'wwn': 'Wwn',
        'wwnn': 'Wwnn',
        'wwpn': 'Wwpn',
        'controller': 'Controller',
        'storage_array': 'StorageArray'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, iqn=None, name=None, speed=None, status='Unknown', type='FC', wwn=None, wwnn=None, wwpn=None, controller=None, storage_array=None):
        """
        StoragePhysicalPort - a model defined in Swagger
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
        self._iqn = None
        self._name = None
        self._speed = None
        self._status = None
        self._type = None
        self._wwn = None
        self._wwnn = None
        self._wwpn = None
        self._controller = None
        self._storage_array = None

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
        if iqn is not None:
          self.iqn = iqn
        if name is not None:
          self.name = name
        if speed is not None:
          self.speed = speed
        if status is not None:
          self.status = status
        if type is not None:
          self.type = type
        if wwn is not None:
          self.wwn = wwn
        if wwnn is not None:
          self.wwnn = wwnn
        if wwpn is not None:
          self.wwpn = wwpn
        if controller is not None:
          self.controller = controller
        if storage_array is not None:
          self.storage_array = storage_array

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StoragePhysicalPort.
        The Account ID for this managed object.  

        :return: The account_moid of this StoragePhysicalPort.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StoragePhysicalPort.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StoragePhysicalPort.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StoragePhysicalPort.
        The time when this managed object was created.  

        :return: The create_time of this StoragePhysicalPort.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StoragePhysicalPort.
        The time when this managed object was created.  

        :param create_time: The create_time of this StoragePhysicalPort.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StoragePhysicalPort.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StoragePhysicalPort.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StoragePhysicalPort.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StoragePhysicalPort.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StoragePhysicalPort.
        The time when this managed object was last modified.  

        :return: The mod_time of this StoragePhysicalPort.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StoragePhysicalPort.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StoragePhysicalPort.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StoragePhysicalPort.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this StoragePhysicalPort.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StoragePhysicalPort.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this StoragePhysicalPort.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StoragePhysicalPort.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this StoragePhysicalPort.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StoragePhysicalPort.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this StoragePhysicalPort.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StoragePhysicalPort.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StoragePhysicalPort.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StoragePhysicalPort.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StoragePhysicalPort.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StoragePhysicalPort.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StoragePhysicalPort.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StoragePhysicalPort.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StoragePhysicalPort.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StoragePhysicalPort.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StoragePhysicalPort.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StoragePhysicalPort.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StoragePhysicalPort.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StoragePhysicalPort.
        The versioning info for this managed object.   

        :return: The version_context of this StoragePhysicalPort.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StoragePhysicalPort.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StoragePhysicalPort.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StoragePhysicalPort.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StoragePhysicalPort.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StoragePhysicalPort.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StoragePhysicalPort.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StoragePhysicalPort.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StoragePhysicalPort.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StoragePhysicalPort.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StoragePhysicalPort.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StoragePhysicalPort.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this StoragePhysicalPort.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StoragePhysicalPort.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this StoragePhysicalPort.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def iqn(self):
        """
        Gets the iqn of this StoragePhysicalPort.
        ISCSI qualified name applicable for ethernet port. eg 'iqn.2008-05.com.storage:fnm00151300643-514f0c50141faf05'.  

        :return: The iqn of this StoragePhysicalPort.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this StoragePhysicalPort.
        ISCSI qualified name applicable for ethernet port. eg 'iqn.2008-05.com.storage:fnm00151300643-514f0c50141faf05'.  

        :param iqn: The iqn of this StoragePhysicalPort.
        :type: str
        """

        self._iqn = iqn

    @property
    def name(self):
        """
        Gets the name of this StoragePhysicalPort.
        Name of the physical port available in storage array.  

        :return: The name of this StoragePhysicalPort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePhysicalPort.
        Name of the physical port available in storage array.  

        :param name: The name of this StoragePhysicalPort.
        :type: str
        """

        self._name = name

    @property
    def speed(self):
        """
        Gets the speed of this StoragePhysicalPort.
        Operational speed of physical port measured in Gbps.  

        :return: The speed of this StoragePhysicalPort.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of this StoragePhysicalPort.
        Operational speed of physical port measured in Gbps.  

        :param speed: The speed of this StoragePhysicalPort.
        :type: int
        """

        self._speed = speed

    @property
    def status(self):
        """
        Gets the status of this StoragePhysicalPort.
        Status of storage array port.  

        :return: The status of this StoragePhysicalPort.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StoragePhysicalPort.
        Status of storage array port.  

        :param status: The status of this StoragePhysicalPort.
        :type: str
        """
        allowed_values = ["Unknown", "Ok", "Degraded", "Critical", "Offline", "Identifying", "NotAvailable", "Updating", "Unrecognized"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this StoragePhysicalPort.
        Port type, it can be a any of the following category FC, FCoE and iSCSI.  

        :return: The type of this StoragePhysicalPort.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StoragePhysicalPort.
        Port type, it can be a any of the following category FC, FCoE and iSCSI.  

        :param type: The type of this StoragePhysicalPort.
        :type: str
        """
        allowed_values = ["FC", "iSCSI", "FCoE"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def wwn(self):
        """
        Gets the wwn of this StoragePhysicalPort.
        World wide name of FC port. It is a combination of WWNN and WWPN represented in 128 bit hexa decimal formatted with colon. e.g '51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01'.  

        :return: The wwn of this StoragePhysicalPort.
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """
        Sets the wwn of this StoragePhysicalPort.
        World wide name of FC port. It is a combination of WWNN and WWPN represented in 128 bit hexa decimal formatted with colon. e.g '51:4f:0c:50:14:1f:af:01:51:4f:0c:51:14:1f:af:01'.  

        :param wwn: The wwn of this StoragePhysicalPort.
        :type: str
        """

        self._wwn = wwn

    @property
    def wwnn(self):
        """
        Gets the wwnn of this StoragePhysicalPort.
        World wide node name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:50:14:1f:af:01'.  

        :return: The wwnn of this StoragePhysicalPort.
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """
        Sets the wwnn of this StoragePhysicalPort.
        World wide node name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:50:14:1f:af:01'.  

        :param wwnn: The wwnn of this StoragePhysicalPort.
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """
        Gets the wwpn of this StoragePhysicalPort.
        World wide port name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:51:14:1f:af:01'.   

        :return: The wwpn of this StoragePhysicalPort.
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """
        Sets the wwpn of this StoragePhysicalPort.
        World wide port name of FC port. Represented in 64 bit digit hexa formatted with colon eg '51:4f:0c:51:14:1f:af:01'.   

        :param wwpn: The wwpn of this StoragePhysicalPort.
        :type: str
        """

        self._wwpn = wwpn

    @property
    def controller(self):
        """
        Gets the controller of this StoragePhysicalPort.
        Parent storage array controller object. 

        :return: The controller of this StoragePhysicalPort.
        :rtype: StorageArrayControllerRef
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this StoragePhysicalPort.
        Parent storage array controller object. 

        :param controller: The controller of this StoragePhysicalPort.
        :type: StorageArrayControllerRef
        """

        self._controller = controller

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StoragePhysicalPort.
        Storage array managed object. 

        :return: The storage_array of this StoragePhysicalPort.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StoragePhysicalPort.
        Storage array managed object. 

        :param storage_array: The storage_array of this StoragePhysicalPort.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

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
        if not isinstance(other, StoragePhysicalPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
