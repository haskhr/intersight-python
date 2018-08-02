# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.7-681
    
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
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'controller': 'ManagementControllerRef',
        'equipment_chassis': 'EquipmentChassisRef',
        'expander_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'controller': 'Controller',
        'equipment_chassis': 'EquipmentChassis',
        'expander_id': 'ExpanderId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, controller=None, equipment_chassis=None, expander_id=None, name=None, oper_state=None, operability=None, presence=None, registered_device=None):
        """
        StorageSasExpander - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._controller = None
        self._equipment_chassis = None
        self._expander_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._registered_device = None

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
        if controller is not None:
          self.controller = controller
        if equipment_chassis is not None:
          self.equipment_chassis = equipment_chassis
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
    def ancestors(self):
        """
        Gets the ancestors of this StorageSasExpander.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageSasExpander.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageSasExpander.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageSasExpander.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

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
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageSasExpander.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageSasExpander.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageSasExpander.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageSasExpander.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageSasExpander.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageSasExpander.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageSasExpander.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageSasExpander.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageSasExpander.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageSasExpander.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageSasExpander.
        :type: list[str]
        """

        self._owners = owners

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
    def tags(self):
        """
        Gets the tags of this StorageSasExpander.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageSasExpander.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageSasExpander.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageSasExpander.
        :type: list[MoTag]
        """

        self._tags = tags

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

        :return: The dn of this StorageSasExpander.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageSasExpander.

        :param dn: The dn of this StorageSasExpander.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageSasExpander.

        :return: The rn of this StorageSasExpander.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageSasExpander.

        :param rn: The rn of this StorageSasExpander.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageSasExpander.

        :return: The model of this StorageSasExpander.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageSasExpander.

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

        :return: The serial of this StorageSasExpander.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageSasExpander.

        :param serial: The serial of this StorageSasExpander.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageSasExpander.

        :return: The vendor of this StorageSasExpander.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageSasExpander.

        :param vendor: The vendor of this StorageSasExpander.
        :type: str
        """

        self._vendor = vendor

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

        :return: The equipment_chassis of this StorageSasExpander.
        :rtype: EquipmentChassisRef
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """
        Sets the equipment_chassis of this StorageSasExpander.

        :param equipment_chassis: The equipment_chassis of this StorageSasExpander.
        :type: EquipmentChassisRef
        """

        self._equipment_chassis = equipment_chassis

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
    def registered_device(self):
        """
        Gets the registered_device of this StorageSasExpander.

        :return: The registered_device of this StorageSasExpander.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageSasExpander.

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
