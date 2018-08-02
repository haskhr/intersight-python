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


class StorageFlexFlashController(object):
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
        'compute_board': 'ComputeBoardRef',
        'controller_state': 'str',
        'ff_controller_id': 'str',
        'flex_flash_controller_props': 'list[StorageFlexFlashControllerPropsRef]',
        'flex_flash_physical_drives': 'list[StorageFlexFlashPhysicalDriveRef]',
        'flex_flash_virtual_drives': 'list[StorageFlexFlashVirtualDriveRef]',
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
        'compute_board': 'ComputeBoard',
        'controller_state': 'ControllerState',
        'ff_controller_id': 'FfControllerId',
        'flex_flash_controller_props': 'FlexFlashControllerProps',
        'flex_flash_physical_drives': 'FlexFlashPhysicalDrives',
        'flex_flash_virtual_drives': 'FlexFlashVirtualDrives',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, compute_board=None, controller_state=None, ff_controller_id=None, flex_flash_controller_props=None, flex_flash_physical_drives=None, flex_flash_virtual_drives=None, registered_device=None):
        """
        StorageFlexFlashController - a model defined in Swagger
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
        self._compute_board = None
        self._controller_state = None
        self._ff_controller_id = None
        self._flex_flash_controller_props = None
        self._flex_flash_physical_drives = None
        self._flex_flash_virtual_drives = None
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
        if compute_board is not None:
          self.compute_board = compute_board
        if controller_state is not None:
          self.controller_state = controller_state
        if ff_controller_id is not None:
          self.ff_controller_id = ff_controller_id
        if flex_flash_controller_props is not None:
          self.flex_flash_controller_props = flex_flash_controller_props
        if flex_flash_physical_drives is not None:
          self.flex_flash_physical_drives = flex_flash_physical_drives
        if flex_flash_virtual_drives is not None:
          self.flex_flash_virtual_drives = flex_flash_virtual_drives
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageFlexFlashController.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageFlexFlashController.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageFlexFlashController.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageFlexFlashController.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageFlexFlashController.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageFlexFlashController.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageFlexFlashController.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageFlexFlashController.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageFlexFlashController.
        The time when this managed object was created.  

        :return: The create_time of this StorageFlexFlashController.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageFlexFlashController.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageFlexFlashController.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageFlexFlashController.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageFlexFlashController.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageFlexFlashController.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageFlexFlashController.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageFlexFlashController.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageFlexFlashController.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageFlexFlashController.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageFlexFlashController.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageFlexFlashController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageFlexFlashController.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageFlexFlashController.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageFlexFlashController.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageFlexFlashController.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageFlexFlashController.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageFlexFlashController.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageFlexFlashController.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageFlexFlashController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageFlexFlashController.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageFlexFlashController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageFlexFlashController.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageFlexFlashController.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageFlexFlashController.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageFlexFlashController.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageFlexFlashController.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageFlexFlashController.

        :return: The device_mo_id of this StorageFlexFlashController.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageFlexFlashController.

        :param device_mo_id: The device_mo_id of this StorageFlexFlashController.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageFlexFlashController.

        :return: The dn of this StorageFlexFlashController.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageFlexFlashController.

        :param dn: The dn of this StorageFlexFlashController.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageFlexFlashController.

        :return: The rn of this StorageFlexFlashController.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageFlexFlashController.

        :param rn: The rn of this StorageFlexFlashController.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageFlexFlashController.

        :return: The model of this StorageFlexFlashController.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageFlexFlashController.

        :param model: The model of this StorageFlexFlashController.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageFlexFlashController.

        :return: The revision of this StorageFlexFlashController.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageFlexFlashController.

        :param revision: The revision of this StorageFlexFlashController.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageFlexFlashController.

        :return: The serial of this StorageFlexFlashController.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageFlexFlashController.

        :param serial: The serial of this StorageFlexFlashController.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageFlexFlashController.

        :return: The vendor of this StorageFlexFlashController.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageFlexFlashController.

        :param vendor: The vendor of this StorageFlexFlashController.
        :type: str
        """

        self._vendor = vendor

    @property
    def compute_board(self):
        """
        Gets the compute_board of this StorageFlexFlashController.

        :return: The compute_board of this StorageFlexFlashController.
        :rtype: ComputeBoardRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this StorageFlexFlashController.

        :param compute_board: The compute_board of this StorageFlexFlashController.
        :type: ComputeBoardRef
        """

        self._compute_board = compute_board

    @property
    def controller_state(self):
        """
        Gets the controller_state of this StorageFlexFlashController.

        :return: The controller_state of this StorageFlexFlashController.
        :rtype: str
        """
        return self._controller_state

    @controller_state.setter
    def controller_state(self, controller_state):
        """
        Sets the controller_state of this StorageFlexFlashController.

        :param controller_state: The controller_state of this StorageFlexFlashController.
        :type: str
        """

        self._controller_state = controller_state

    @property
    def ff_controller_id(self):
        """
        Gets the ff_controller_id of this StorageFlexFlashController.

        :return: The ff_controller_id of this StorageFlexFlashController.
        :rtype: str
        """
        return self._ff_controller_id

    @ff_controller_id.setter
    def ff_controller_id(self, ff_controller_id):
        """
        Sets the ff_controller_id of this StorageFlexFlashController.

        :param ff_controller_id: The ff_controller_id of this StorageFlexFlashController.
        :type: str
        """

        self._ff_controller_id = ff_controller_id

    @property
    def flex_flash_controller_props(self):
        """
        Gets the flex_flash_controller_props of this StorageFlexFlashController.

        :return: The flex_flash_controller_props of this StorageFlexFlashController.
        :rtype: list[StorageFlexFlashControllerPropsRef]
        """
        return self._flex_flash_controller_props

    @flex_flash_controller_props.setter
    def flex_flash_controller_props(self, flex_flash_controller_props):
        """
        Sets the flex_flash_controller_props of this StorageFlexFlashController.

        :param flex_flash_controller_props: The flex_flash_controller_props of this StorageFlexFlashController.
        :type: list[StorageFlexFlashControllerPropsRef]
        """

        self._flex_flash_controller_props = flex_flash_controller_props

    @property
    def flex_flash_physical_drives(self):
        """
        Gets the flex_flash_physical_drives of this StorageFlexFlashController.

        :return: The flex_flash_physical_drives of this StorageFlexFlashController.
        :rtype: list[StorageFlexFlashPhysicalDriveRef]
        """
        return self._flex_flash_physical_drives

    @flex_flash_physical_drives.setter
    def flex_flash_physical_drives(self, flex_flash_physical_drives):
        """
        Sets the flex_flash_physical_drives of this StorageFlexFlashController.

        :param flex_flash_physical_drives: The flex_flash_physical_drives of this StorageFlexFlashController.
        :type: list[StorageFlexFlashPhysicalDriveRef]
        """

        self._flex_flash_physical_drives = flex_flash_physical_drives

    @property
    def flex_flash_virtual_drives(self):
        """
        Gets the flex_flash_virtual_drives of this StorageFlexFlashController.

        :return: The flex_flash_virtual_drives of this StorageFlexFlashController.
        :rtype: list[StorageFlexFlashVirtualDriveRef]
        """
        return self._flex_flash_virtual_drives

    @flex_flash_virtual_drives.setter
    def flex_flash_virtual_drives(self, flex_flash_virtual_drives):
        """
        Sets the flex_flash_virtual_drives of this StorageFlexFlashController.

        :param flex_flash_virtual_drives: The flex_flash_virtual_drives of this StorageFlexFlashController.
        :type: list[StorageFlexFlashVirtualDriveRef]
        """

        self._flex_flash_virtual_drives = flex_flash_virtual_drives

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageFlexFlashController.

        :return: The registered_device of this StorageFlexFlashController.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageFlexFlashController.

        :param registered_device: The registered_device of this StorageFlexFlashController.
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
        if not isinstance(other, StorageFlexFlashController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
