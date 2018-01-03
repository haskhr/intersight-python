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


class MemoryArray(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'array_id': 'int',
        'compute_board': 'MoMoRef',
        'cpu_id': 'int',
        'current_capacity': 'str',
        'error_correction': 'str',
        'max_capacity': 'str',
        'max_devices': 'str',
        'oper_power_state': 'str',
        'presence': 'str',
        'registered_device': 'MoMoRef',
        'units': 'list[MoMoRef]'
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
        'array_id': 'ArrayId',
        'compute_board': 'ComputeBoard',
        'cpu_id': 'CpuId',
        'current_capacity': 'CurrentCapacity',
        'error_correction': 'ErrorCorrection',
        'max_capacity': 'MaxCapacity',
        'max_devices': 'MaxDevices',
        'oper_power_state': 'OperPowerState',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'units': 'Units'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, array_id=None, compute_board=None, cpu_id=None, current_capacity=None, error_correction=None, max_capacity=None, max_devices=None, oper_power_state=None, presence=None, registered_device=None, units=None):
        """
        MemoryArray - a model defined in Swagger
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
        self._array_id = None
        self._compute_board = None
        self._cpu_id = None
        self._current_capacity = None
        self._error_correction = None
        self._max_capacity = None
        self._max_devices = None
        self._oper_power_state = None
        self._presence = None
        self._registered_device = None
        self._units = None

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
        if array_id is not None:
          self.array_id = array_id
        if compute_board is not None:
          self.compute_board = compute_board
        if cpu_id is not None:
          self.cpu_id = cpu_id
        if current_capacity is not None:
          self.current_capacity = current_capacity
        if error_correction is not None:
          self.error_correction = error_correction
        if max_capacity is not None:
          self.max_capacity = max_capacity
        if max_devices is not None:
          self.max_devices = max_devices
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if units is not None:
          self.units = units

    @property
    def account_moid(self):
        """
        Gets the account_moid of this MemoryArray.
        The Account ID for this managed object.  

        :return: The account_moid of this MemoryArray.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this MemoryArray.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this MemoryArray.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this MemoryArray.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this MemoryArray.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this MemoryArray.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this MemoryArray.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this MemoryArray.
        The time when this managed object was created.  

        :return: The create_time of this MemoryArray.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this MemoryArray.
        The time when this managed object was created.  

        :param create_time: The create_time of this MemoryArray.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this MemoryArray.
        The time when this managed object was last modified.  

        :return: The mod_time of this MemoryArray.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this MemoryArray.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this MemoryArray.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this MemoryArray.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this MemoryArray.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this MemoryArray.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this MemoryArray.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this MemoryArray.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this MemoryArray.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MemoryArray.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this MemoryArray.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this MemoryArray.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this MemoryArray.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this MemoryArray.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this MemoryArray.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this MemoryArray.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this MemoryArray.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this MemoryArray.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this MemoryArray.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this MemoryArray.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this MemoryArray.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MemoryArray.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this MemoryArray.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this MemoryArray.

        :return: The device_mo_id of this MemoryArray.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this MemoryArray.

        :param device_mo_id: The device_mo_id of this MemoryArray.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this MemoryArray.

        :return: The dn of this MemoryArray.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this MemoryArray.

        :param dn: The dn of this MemoryArray.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this MemoryArray.

        :return: The rn of this MemoryArray.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this MemoryArray.

        :param rn: The rn of this MemoryArray.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this MemoryArray.

        :return: The model of this MemoryArray.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this MemoryArray.

        :param model: The model of this MemoryArray.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this MemoryArray.

        :return: The revision of this MemoryArray.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this MemoryArray.

        :param revision: The revision of this MemoryArray.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this MemoryArray.

        :return: The serial of this MemoryArray.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this MemoryArray.

        :param serial: The serial of this MemoryArray.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this MemoryArray.

        :return: The vendor of this MemoryArray.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this MemoryArray.

        :param vendor: The vendor of this MemoryArray.
        :type: str
        """

        self._vendor = vendor

    @property
    def array_id(self):
        """
        Gets the array_id of this MemoryArray.

        :return: The array_id of this MemoryArray.
        :rtype: int
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """
        Sets the array_id of this MemoryArray.

        :param array_id: The array_id of this MemoryArray.
        :type: int
        """

        self._array_id = array_id

    @property
    def compute_board(self):
        """
        Gets the compute_board of this MemoryArray.

        :return: The compute_board of this MemoryArray.
        :rtype: MoMoRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this MemoryArray.

        :param compute_board: The compute_board of this MemoryArray.
        :type: MoMoRef
        """

        self._compute_board = compute_board

    @property
    def cpu_id(self):
        """
        Gets the cpu_id of this MemoryArray.

        :return: The cpu_id of this MemoryArray.
        :rtype: int
        """
        return self._cpu_id

    @cpu_id.setter
    def cpu_id(self, cpu_id):
        """
        Sets the cpu_id of this MemoryArray.

        :param cpu_id: The cpu_id of this MemoryArray.
        :type: int
        """

        self._cpu_id = cpu_id

    @property
    def current_capacity(self):
        """
        Gets the current_capacity of this MemoryArray.

        :return: The current_capacity of this MemoryArray.
        :rtype: str
        """
        return self._current_capacity

    @current_capacity.setter
    def current_capacity(self, current_capacity):
        """
        Sets the current_capacity of this MemoryArray.

        :param current_capacity: The current_capacity of this MemoryArray.
        :type: str
        """

        self._current_capacity = current_capacity

    @property
    def error_correction(self):
        """
        Gets the error_correction of this MemoryArray.

        :return: The error_correction of this MemoryArray.
        :rtype: str
        """
        return self._error_correction

    @error_correction.setter
    def error_correction(self, error_correction):
        """
        Sets the error_correction of this MemoryArray.

        :param error_correction: The error_correction of this MemoryArray.
        :type: str
        """

        self._error_correction = error_correction

    @property
    def max_capacity(self):
        """
        Gets the max_capacity of this MemoryArray.

        :return: The max_capacity of this MemoryArray.
        :rtype: str
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """
        Sets the max_capacity of this MemoryArray.

        :param max_capacity: The max_capacity of this MemoryArray.
        :type: str
        """

        self._max_capacity = max_capacity

    @property
    def max_devices(self):
        """
        Gets the max_devices of this MemoryArray.

        :return: The max_devices of this MemoryArray.
        :rtype: str
        """
        return self._max_devices

    @max_devices.setter
    def max_devices(self, max_devices):
        """
        Sets the max_devices of this MemoryArray.

        :param max_devices: The max_devices of this MemoryArray.
        :type: str
        """

        self._max_devices = max_devices

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this MemoryArray.

        :return: The oper_power_state of this MemoryArray.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this MemoryArray.

        :param oper_power_state: The oper_power_state of this MemoryArray.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def presence(self):
        """
        Gets the presence of this MemoryArray.

        :return: The presence of this MemoryArray.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this MemoryArray.

        :param presence: The presence of this MemoryArray.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this MemoryArray.

        :return: The registered_device of this MemoryArray.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this MemoryArray.

        :param registered_device: The registered_device of this MemoryArray.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def units(self):
        """
        Gets the units of this MemoryArray.

        :return: The units of this MemoryArray.
        :rtype: list[MoMoRef]
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this MemoryArray.

        :param units: The units of this MemoryArray.
        :type: list[MoMoRef]
        """

        self._units = units

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
        if not isinstance(other, MemoryArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
