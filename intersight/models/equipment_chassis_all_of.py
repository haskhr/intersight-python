# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class EquipmentChassisAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'chassis_id': 'int',
        'connection_path': 'str',
        'connection_status': 'str',
        'description': 'str',
        'fault_summary': 'int',
        'name': 'str',
        'oper_state': 'str',
        'part_number': 'str',
        'pid': 'str',
        'platform_type': 'str',
        'product_name': 'str',
        'sku': 'str',
        'vid': 'str',
        'blades': 'list[ComputeBlade]',
        'fanmodules': 'list[EquipmentFanModule]',
        'ioms': 'list[EquipmentIoCard]',
        'psus': 'list[EquipmentPsu]',
        'registered_device': 'AssetDeviceRegistration',
        'sasexpanders': 'list[StorageSasExpander]',
        'siocs': 'list[EquipmentSystemIoController]',
        'storage_enclosures': 'list[StorageEnclosure]'
    }

    attribute_map = {
        'chassis_id': 'ChassisId',
        'connection_path': 'ConnectionPath',
        'connection_status': 'ConnectionStatus',
        'description': 'Description',
        'fault_summary': 'FaultSummary',
        'name': 'Name',
        'oper_state': 'OperState',
        'part_number': 'PartNumber',
        'pid': 'Pid',
        'platform_type': 'PlatformType',
        'product_name': 'ProductName',
        'sku': 'Sku',
        'vid': 'Vid',
        'blades': 'Blades',
        'fanmodules': 'Fanmodules',
        'ioms': 'Ioms',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'sasexpanders': 'Sasexpanders',
        'siocs': 'Siocs',
        'storage_enclosures': 'StorageEnclosures'
    }

    def __init__(self,
                 chassis_id=None,
                 connection_path=None,
                 connection_status=None,
                 description=None,
                 fault_summary=None,
                 name=None,
                 oper_state=None,
                 part_number=None,
                 pid=None,
                 platform_type=None,
                 product_name=None,
                 sku=None,
                 vid=None,
                 blades=None,
                 fanmodules=None,
                 ioms=None,
                 psus=None,
                 registered_device=None,
                 sasexpanders=None,
                 siocs=None,
                 storage_enclosures=None,
                 local_vars_configuration=None):  # noqa: E501
        """EquipmentChassisAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chassis_id = None
        self._connection_path = None
        self._connection_status = None
        self._description = None
        self._fault_summary = None
        self._name = None
        self._oper_state = None
        self._part_number = None
        self._pid = None
        self._platform_type = None
        self._product_name = None
        self._sku = None
        self._vid = None
        self._blades = None
        self._fanmodules = None
        self._ioms = None
        self._psus = None
        self._registered_device = None
        self._sasexpanders = None
        self._siocs = None
        self._storage_enclosures = None
        self.discriminator = None

        if chassis_id is not None:
            self.chassis_id = chassis_id
        if connection_path is not None:
            self.connection_path = connection_path
        if connection_status is not None:
            self.connection_status = connection_status
        if description is not None:
            self.description = description
        if fault_summary is not None:
            self.fault_summary = fault_summary
        if name is not None:
            self.name = name
        if oper_state is not None:
            self.oper_state = oper_state
        if part_number is not None:
            self.part_number = part_number
        if pid is not None:
            self.pid = pid
        if platform_type is not None:
            self.platform_type = platform_type
        if product_name is not None:
            self.product_name = product_name
        if sku is not None:
            self.sku = sku
        if vid is not None:
            self.vid = vid
        if blades is not None:
            self.blades = blades
        if fanmodules is not None:
            self.fanmodules = fanmodules
        if ioms is not None:
            self.ioms = ioms
        if psus is not None:
            self.psus = psus
        if registered_device is not None:
            self.registered_device = registered_device
        if sasexpanders is not None:
            self.sasexpanders = sasexpanders
        if siocs is not None:
            self.siocs = siocs
        if storage_enclosures is not None:
            self.storage_enclosures = storage_enclosures

    @property
    def chassis_id(self):
        """Gets the chassis_id of this EquipmentChassisAllOf.  # noqa: E501

        The assigned identifier for a chassis.    # noqa: E501

        :return: The chassis_id of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: int
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """Sets the chassis_id of this EquipmentChassisAllOf.

        The assigned identifier for a chassis.    # noqa: E501

        :param chassis_id: The chassis_id of this EquipmentChassisAllOf.  # noqa: E501
        :type: int
        """

        self._chassis_id = chassis_id

    @property
    def connection_path(self):
        """Gets the connection_path of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the connectivity path for the chassis enclosure.    # noqa: E501

        :return: The connection_path of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._connection_path

    @connection_path.setter
    def connection_path(self, connection_path):
        """Sets the connection_path of this EquipmentChassisAllOf.

        This field identifies the connectivity path for the chassis enclosure.    # noqa: E501

        :param connection_path: The connection_path of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._connection_path = connection_path

    @property
    def connection_status(self):
        """Gets the connection_status of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the connectivity status for the chassis enclosure.    # noqa: E501

        :return: The connection_status of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this EquipmentChassisAllOf.

        This field identifies the connectivity status for the chassis enclosure.    # noqa: E501

        :param connection_status: The connection_status of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._connection_status = connection_status

    @property
    def description(self):
        """Gets the description of this EquipmentChassisAllOf.  # noqa: E501

        This field is to provide description for chassis model.    # noqa: E501

        :return: The description of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EquipmentChassisAllOf.

        This field is to provide description for chassis model.    # noqa: E501

        :param description: The description of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fault_summary(self):
        """Gets the fault_summary of this EquipmentChassisAllOf.  # noqa: E501


        :return: The fault_summary of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """Sets the fault_summary of this EquipmentChassisAllOf.


        :param fault_summary: The fault_summary of this EquipmentChassisAllOf.  # noqa: E501
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def name(self):
        """Gets the name of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the name for the chassis enclosure.    # noqa: E501

        :return: The name of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EquipmentChassisAllOf.

        This field identifies the name for the chassis enclosure.    # noqa: E501

        :param name: The name of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """Gets the oper_state of this EquipmentChassisAllOf.  # noqa: E501


        :return: The oper_state of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this EquipmentChassisAllOf.


        :param oper_state: The oper_state of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def part_number(self):
        """Gets the part_number of this EquipmentChassisAllOf.  # noqa: E501

        Part Number identifier for the chassis enclosure.    # noqa: E501

        :return: The part_number of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this EquipmentChassisAllOf.

        Part Number identifier for the chassis enclosure.    # noqa: E501

        :param part_number: The part_number of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def pid(self):
        """Gets the pid of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the Product ID for the chassis enclosure.    # noqa: E501

        :return: The pid of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this EquipmentChassisAllOf.

        This field identifies the Product ID for the chassis enclosure.    # noqa: E501

        :param pid: The pid of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def platform_type(self):
        """Gets the platform_type of this EquipmentChassisAllOf.  # noqa: E501


        :return: The platform_type of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this EquipmentChassisAllOf.


        :param platform_type: The platform_type of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._platform_type = platform_type

    @property
    def product_name(self):
        """Gets the product_name of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the Product Name for the chassis enclosure.    # noqa: E501

        :return: The product_name of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this EquipmentChassisAllOf.

        This field identifies the Product Name for the chassis enclosure.    # noqa: E501

        :param product_name: The product_name of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def sku(self):
        """Gets the sku of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the Stock Keeping Unit for the chassis enclosure.    # noqa: E501

        :return: The sku of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this EquipmentChassisAllOf.

        This field identifies the Stock Keeping Unit for the chassis enclosure.    # noqa: E501

        :param sku: The sku of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def vid(self):
        """Gets the vid of this EquipmentChassisAllOf.  # noqa: E501

        This field identifies the Vendor ID for the chassis enclosure.     # noqa: E501

        :return: The vid of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this EquipmentChassisAllOf.

        This field identifies the Vendor ID for the chassis enclosure.     # noqa: E501

        :param vid: The vid of this EquipmentChassisAllOf.  # noqa: E501
        :type: str
        """

        self._vid = vid

    @property
    def blades(self):
        """Gets the blades of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a computeBlade resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The blades of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[ComputeBlade]
        """
        return self._blades

    @blades.setter
    def blades(self, blades):
        """Sets the blades of this EquipmentChassisAllOf.

        A reference to a computeBlade resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param blades: The blades of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[ComputeBlade]
        """

        self._blades = blades

    @property
    def fanmodules(self):
        """Gets the fanmodules of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The fanmodules of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[EquipmentFanModule]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """Sets the fanmodules of this EquipmentChassisAllOf.

        A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param fanmodules: The fanmodules of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[EquipmentFanModule]
        """

        self._fanmodules = fanmodules

    @property
    def ioms(self):
        """Gets the ioms of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a equipmentIoCard resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The ioms of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[EquipmentIoCard]
        """
        return self._ioms

    @ioms.setter
    def ioms(self, ioms):
        """Sets the ioms of this EquipmentChassisAllOf.

        A reference to a equipmentIoCard resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param ioms: The ioms of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[EquipmentIoCard]
        """

        self._ioms = ioms

    @property
    def psus(self):
        """Gets the psus of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The psus of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[EquipmentPsu]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """Sets the psus of this EquipmentChassisAllOf.

        A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param psus: The psus of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[EquipmentPsu]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """Gets the registered_device of this EquipmentChassisAllOf.  # noqa: E501


        :return: The registered_device of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this EquipmentChassisAllOf.


        :param registered_device: The registered_device of this EquipmentChassisAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def sasexpanders(self):
        """Gets the sasexpanders of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a storageSasExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The sasexpanders of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[StorageSasExpander]
        """
        return self._sasexpanders

    @sasexpanders.setter
    def sasexpanders(self, sasexpanders):
        """Sets the sasexpanders of this EquipmentChassisAllOf.

        A reference to a storageSasExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param sasexpanders: The sasexpanders of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[StorageSasExpander]
        """

        self._sasexpanders = sasexpanders

    @property
    def siocs(self):
        """Gets the siocs of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a equipmentSystemIoController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The siocs of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[EquipmentSystemIoController]
        """
        return self._siocs

    @siocs.setter
    def siocs(self, siocs):
        """Sets the siocs of this EquipmentChassisAllOf.

        A reference to a equipmentSystemIoController resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param siocs: The siocs of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[EquipmentSystemIoController]
        """

        self._siocs = siocs

    @property
    def storage_enclosures(self):
        """Gets the storage_enclosures of this EquipmentChassisAllOf.  # noqa: E501

        A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline. This field identifies the chassis enclosures.   # noqa: E501

        :return: The storage_enclosures of this EquipmentChassisAllOf.  # noqa: E501
        :rtype: list[StorageEnclosure]
        """
        return self._storage_enclosures

    @storage_enclosures.setter
    def storage_enclosures(self, storage_enclosures):
        """Sets the storage_enclosures of this EquipmentChassisAllOf.

        A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline. This field identifies the chassis enclosures.   # noqa: E501

        :param storage_enclosures: The storage_enclosures of this EquipmentChassisAllOf.  # noqa: E501
        :type: list[StorageEnclosure]
        """

        self._storage_enclosures = storage_enclosures

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EquipmentChassisAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentChassisAllOf):
            return True

        return self.to_dict() != other.to_dict()