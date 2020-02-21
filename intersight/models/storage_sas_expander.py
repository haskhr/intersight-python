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


class StorageSasExpander(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'expander_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'sas_address': 'str',
        'controller': 'ManagementControllerRef',
        'equipment_chassis': 'EquipmentChassisRef',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'expander_id': 'ExpanderId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'sas_address': 'SasAddress',
        'controller': 'Controller',
        'equipment_chassis': 'EquipmentChassis',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, expander_id=None, name=None, oper_state=None, operability=None, presence=None, sas_address=None, controller=None, equipment_chassis=None, registered_device=None):
        """
        StorageSasExpander - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._expander_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._sas_address = None
        self._controller = None
        self._equipment_chassis = None
        self._registered_device = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if expander_id is not None:
          self.expander_id = expander_id
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if presence is not None:
          self.presence = presence
        if sas_address is not None:
          self.sas_address = sas_address
        if controller is not None:
          self.controller = controller
        if equipment_chassis is not None:
          self.equipment_chassis = equipment_chassis
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageSasExpander.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageSasExpander.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageSasExpander.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageSasExpander.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageSasExpander.
        The time when this managed object was created.  

        :return: The create_time of this StorageSasExpander.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageSasExpander.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageSasExpander.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageSasExpander.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageSasExpander.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageSasExpander.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageSasExpander.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageSasExpander.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageSasExpander.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageSasExpander.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageSasExpander.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageSasExpander.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this StorageSasExpander.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageSasExpander.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this StorageSasExpander.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageSasExpander.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this StorageSasExpander.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageSasExpander.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this StorageSasExpander.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageSasExpander.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageSasExpander.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageSasExpander.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageSasExpander.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageSasExpander.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageSasExpander.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageSasExpander.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageSasExpander.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageSasExpander.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageSasExpander.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageSasExpander.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageSasExpander.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageSasExpander.
        The versioning info for this managed object.   

        :return: The version_context of this StorageSasExpander.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageSasExpander.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageSasExpander.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageSasExpander.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageSasExpander.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageSasExpander.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageSasExpander.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StorageSasExpander.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageSasExpander.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageSasExpander.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageSasExpander.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StorageSasExpander.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this StorageSasExpander.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StorageSasExpander.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this StorageSasExpander.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageSasExpander.

        :return: The device_mo_id of this StorageSasExpander.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageSasExpander.

        :param device_mo_id: The device_mo_id of this StorageSasExpander.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageSasExpander.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this StorageSasExpander.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageSasExpander.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this StorageSasExpander.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageSasExpander.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this StorageSasExpander.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageSasExpander.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this StorageSasExpander.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageSasExpander.
        This field identifies the model of the given component.  

        :return: The model of this StorageSasExpander.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageSasExpander.
        This field identifies the model of the given component.  

        :param model: The model of this StorageSasExpander.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageSasExpander.

        :return: The revision of this StorageSasExpander.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageSasExpander.

        :param revision: The revision of this StorageSasExpander.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageSasExpander.
        This field identifies the serial of the given component.  

        :return: The serial of this StorageSasExpander.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageSasExpander.
        This field identifies the serial of the given component.  

        :param serial: The serial of this StorageSasExpander.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageSasExpander.
        This field identifies the vendor of the given component.   

        :return: The vendor of this StorageSasExpander.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageSasExpander.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this StorageSasExpander.
        :type: str
        """

        self._vendor = vendor

    @property
    def expander_id(self):
        """
        Gets the expander_id of this StorageSasExpander.

        :return: The expander_id of this StorageSasExpander.
        :rtype: int
        """
        return self._expander_id

    @expander_id.setter
    def expander_id(self, expander_id):
        """
        Sets the expander_id of this StorageSasExpander.

        :param expander_id: The expander_id of this StorageSasExpander.
        :type: int
        """

        self._expander_id = expander_id

    @property
    def name(self):
        """
        Gets the name of this StorageSasExpander.

        :return: The name of this StorageSasExpander.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageSasExpander.

        :param name: The name of this StorageSasExpander.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this StorageSasExpander.

        :return: The oper_state of this StorageSasExpander.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this StorageSasExpander.

        :param oper_state: The oper_state of this StorageSasExpander.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this StorageSasExpander.

        :return: The operability of this StorageSasExpander.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this StorageSasExpander.

        :param operability: The operability of this StorageSasExpander.
        :type: str
        """

        self._operability = operability

    @property
    def presence(self):
        """
        Gets the presence of this StorageSasExpander.

        :return: The presence of this StorageSasExpander.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this StorageSasExpander.

        :param presence: The presence of this StorageSasExpander.
        :type: str
        """

        self._presence = presence

    @property
    def sas_address(self):
        """
        Gets the sas_address of this StorageSasExpander.

        :return: The sas_address of this StorageSasExpander.
        :rtype: str
        """
        return self._sas_address

    @sas_address.setter
    def sas_address(self, sas_address):
        """
        Sets the sas_address of this StorageSasExpander.

        :param sas_address: The sas_address of this StorageSasExpander.
        :type: str
        """

        self._sas_address = sas_address

    @property
    def controller(self):
        """
        Gets the controller of this StorageSasExpander.

        :return: The controller of this StorageSasExpander.
        :rtype: ManagementControllerRef
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this StorageSasExpander.

        :param controller: The controller of this StorageSasExpander.
        :type: ManagementControllerRef
        """

        self._controller = controller

    @property
    def equipment_chassis(self):
        """
        Gets the equipment_chassis of this StorageSasExpander.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :return: The equipment_chassis of this StorageSasExpander.
        :rtype: EquipmentChassisRef
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """
        Sets the equipment_chassis of this StorageSasExpander.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :param equipment_chassis: The equipment_chassis of this StorageSasExpander.
        :type: EquipmentChassisRef
        """

        self._equipment_chassis = equipment_chassis

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageSasExpander.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this StorageSasExpander.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageSasExpander.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this StorageSasExpander.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, StorageSasExpander):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
