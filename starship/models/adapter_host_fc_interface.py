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


class AdapterHostFcInterface(object):
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
        'adapter_unit': 'MoMoRef',
        'admin_state': 'str',
        'ep_dn': 'str',
        'host_fc_interface_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'original_wwnn': 'str',
        'original_wwpn': 'str',
        'peer_dn': 'str',
        'registered_device': 'MoMoRef',
        'wwnn': 'str',
        'wwpn': 'str'
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
        'adapter_unit': 'AdapterUnit',
        'admin_state': 'AdminState',
        'ep_dn': 'EpDn',
        'host_fc_interface_id': 'HostFcInterfaceId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'original_wwnn': 'OriginalWwnn',
        'original_wwpn': 'OriginalWwpn',
        'peer_dn': 'PeerDn',
        'registered_device': 'RegisteredDevice',
        'wwnn': 'Wwnn',
        'wwpn': 'Wwpn'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, adapter_unit=None, admin_state=None, ep_dn=None, host_fc_interface_id=None, name=None, oper_state=None, operability=None, original_wwnn=None, original_wwpn=None, peer_dn=None, registered_device=None, wwnn=None, wwpn=None):
        """
        AdapterHostFcInterface - a model defined in Swagger
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
        self._adapter_unit = None
        self._admin_state = None
        self._ep_dn = None
        self._host_fc_interface_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._original_wwnn = None
        self._original_wwpn = None
        self._peer_dn = None
        self._registered_device = None
        self._wwnn = None
        self._wwpn = None

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
        if adapter_unit is not None:
          self.adapter_unit = adapter_unit
        if admin_state is not None:
          self.admin_state = admin_state
        if ep_dn is not None:
          self.ep_dn = ep_dn
        if host_fc_interface_id is not None:
          self.host_fc_interface_id = host_fc_interface_id
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if original_wwnn is not None:
          self.original_wwnn = original_wwnn
        if original_wwpn is not None:
          self.original_wwpn = original_wwpn
        if peer_dn is not None:
          self.peer_dn = peer_dn
        if registered_device is not None:
          self.registered_device = registered_device
        if wwnn is not None:
          self.wwnn = wwnn
        if wwpn is not None:
          self.wwpn = wwpn

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AdapterHostFcInterface.
        The Account ID for this managed object.  

        :return: The account_moid of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AdapterHostFcInterface.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this AdapterHostFcInterface.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AdapterHostFcInterface.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this AdapterHostFcInterface.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AdapterHostFcInterface.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this AdapterHostFcInterface.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this AdapterHostFcInterface.
        The time when this managed object was created.  

        :return: The create_time of this AdapterHostFcInterface.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AdapterHostFcInterface.
        The time when this managed object was created.  

        :param create_time: The create_time of this AdapterHostFcInterface.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AdapterHostFcInterface.
        The time when this managed object was last modified.  

        :return: The mod_time of this AdapterHostFcInterface.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AdapterHostFcInterface.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this AdapterHostFcInterface.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AdapterHostFcInterface.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AdapterHostFcInterface.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this AdapterHostFcInterface.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterHostFcInterface.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterHostFcInterface.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this AdapterHostFcInterface.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AdapterHostFcInterface.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this AdapterHostFcInterface.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AdapterHostFcInterface.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this AdapterHostFcInterface.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this AdapterHostFcInterface.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this AdapterHostFcInterface.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AdapterHostFcInterface.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this AdapterHostFcInterface.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this AdapterHostFcInterface.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this AdapterHostFcInterface.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AdapterHostFcInterface.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this AdapterHostFcInterface.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this AdapterHostFcInterface.

        :return: The device_mo_id of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this AdapterHostFcInterface.

        :param device_mo_id: The device_mo_id of this AdapterHostFcInterface.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this AdapterHostFcInterface.

        :return: The dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this AdapterHostFcInterface.

        :param dn: The dn of this AdapterHostFcInterface.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this AdapterHostFcInterface.

        :return: The rn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this AdapterHostFcInterface.

        :param rn: The rn of this AdapterHostFcInterface.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this AdapterHostFcInterface.

        :return: The model of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this AdapterHostFcInterface.

        :param model: The model of this AdapterHostFcInterface.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this AdapterHostFcInterface.

        :return: The revision of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AdapterHostFcInterface.

        :param revision: The revision of this AdapterHostFcInterface.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this AdapterHostFcInterface.

        :return: The serial of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this AdapterHostFcInterface.

        :param serial: The serial of this AdapterHostFcInterface.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this AdapterHostFcInterface.

        :return: The vendor of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this AdapterHostFcInterface.

        :param vendor: The vendor of this AdapterHostFcInterface.
        :type: str
        """

        self._vendor = vendor

    @property
    def adapter_unit(self):
        """
        Gets the adapter_unit of this AdapterHostFcInterface.

        :return: The adapter_unit of this AdapterHostFcInterface.
        :rtype: MoMoRef
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """
        Sets the adapter_unit of this AdapterHostFcInterface.

        :param adapter_unit: The adapter_unit of this AdapterHostFcInterface.
        :type: MoMoRef
        """

        self._adapter_unit = adapter_unit

    @property
    def admin_state(self):
        """
        Gets the admin_state of this AdapterHostFcInterface.

        :return: The admin_state of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this AdapterHostFcInterface.

        :param admin_state: The admin_state of this AdapterHostFcInterface.
        :type: str
        """

        self._admin_state = admin_state

    @property
    def ep_dn(self):
        """
        Gets the ep_dn of this AdapterHostFcInterface.

        :return: The ep_dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._ep_dn

    @ep_dn.setter
    def ep_dn(self, ep_dn):
        """
        Sets the ep_dn of this AdapterHostFcInterface.

        :param ep_dn: The ep_dn of this AdapterHostFcInterface.
        :type: str
        """

        self._ep_dn = ep_dn

    @property
    def host_fc_interface_id(self):
        """
        Gets the host_fc_interface_id of this AdapterHostFcInterface.

        :return: The host_fc_interface_id of this AdapterHostFcInterface.
        :rtype: int
        """
        return self._host_fc_interface_id

    @host_fc_interface_id.setter
    def host_fc_interface_id(self, host_fc_interface_id):
        """
        Sets the host_fc_interface_id of this AdapterHostFcInterface.

        :param host_fc_interface_id: The host_fc_interface_id of this AdapterHostFcInterface.
        :type: int
        """

        self._host_fc_interface_id = host_fc_interface_id

    @property
    def name(self):
        """
        Gets the name of this AdapterHostFcInterface.

        :return: The name of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AdapterHostFcInterface.

        :param name: The name of this AdapterHostFcInterface.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this AdapterHostFcInterface.

        :return: The oper_state of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this AdapterHostFcInterface.

        :param oper_state: The oper_state of this AdapterHostFcInterface.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this AdapterHostFcInterface.

        :return: The operability of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this AdapterHostFcInterface.

        :param operability: The operability of this AdapterHostFcInterface.
        :type: str
        """

        self._operability = operability

    @property
    def original_wwnn(self):
        """
        Gets the original_wwnn of this AdapterHostFcInterface.

        :return: The original_wwnn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._original_wwnn

    @original_wwnn.setter
    def original_wwnn(self, original_wwnn):
        """
        Sets the original_wwnn of this AdapterHostFcInterface.

        :param original_wwnn: The original_wwnn of this AdapterHostFcInterface.
        :type: str
        """

        self._original_wwnn = original_wwnn

    @property
    def original_wwpn(self):
        """
        Gets the original_wwpn of this AdapterHostFcInterface.

        :return: The original_wwpn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._original_wwpn

    @original_wwpn.setter
    def original_wwpn(self, original_wwpn):
        """
        Sets the original_wwpn of this AdapterHostFcInterface.

        :param original_wwpn: The original_wwpn of this AdapterHostFcInterface.
        :type: str
        """

        self._original_wwpn = original_wwpn

    @property
    def peer_dn(self):
        """
        Gets the peer_dn of this AdapterHostFcInterface.

        :return: The peer_dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._peer_dn

    @peer_dn.setter
    def peer_dn(self, peer_dn):
        """
        Sets the peer_dn of this AdapterHostFcInterface.

        :param peer_dn: The peer_dn of this AdapterHostFcInterface.
        :type: str
        """

        self._peer_dn = peer_dn

    @property
    def registered_device(self):
        """
        Gets the registered_device of this AdapterHostFcInterface.

        :return: The registered_device of this AdapterHostFcInterface.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this AdapterHostFcInterface.

        :param registered_device: The registered_device of this AdapterHostFcInterface.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def wwnn(self):
        """
        Gets the wwnn of this AdapterHostFcInterface.

        :return: The wwnn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """
        Sets the wwnn of this AdapterHostFcInterface.

        :param wwnn: The wwnn of this AdapterHostFcInterface.
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """
        Gets the wwpn of this AdapterHostFcInterface.

        :return: The wwpn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """
        Sets the wwpn of this AdapterHostFcInterface.

        :param wwpn: The wwpn of this AdapterHostFcInterface.
        :type: str
        """

        self._wwpn = wwpn

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
        if not isinstance(other, AdapterHostFcInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
