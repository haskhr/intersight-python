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


class HyperflexClusterProfile(object):
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
        'description': 'str',
        'name': 'str',
        'src_template': 'MoMoRef',
        'type': 'str',
        'action': 'str',
        'config_context': 'PolicyConfigContext',
        'account': 'MoMoRef',
        'advanced_storage_config': 'MoMoRef',
        'auto_support': 'MoMoRef',
        'config_result': 'MoMoRef',
        'data_ip_address': 'str',
        'ext_fc_storage': 'MoMoRef',
        'ext_iscsi_storage': 'MoMoRef',
        'hypervisor_type': 'str',
        'local_credential': 'MoMoRef',
        'mac_address_prefix': 'str',
        'mgmt_ip_address': 'str',
        'mgmt_platform': 'str',
        'network_config': 'MoMoRef',
        'node_config': 'MoMoRef',
        'node_profile_config': 'list[MoMoRef]',
        'replication': 'int',
        'storage_data_vlan': 'HyperflexNamedVlan',
        'sys_config': 'MoMoRef',
        'ucsm_config': 'MoMoRef',
        'vcenter_config': 'MoMoRef'
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
        'description': 'Description',
        'name': 'Name',
        'src_template': 'SrcTemplate',
        'type': 'Type',
        'action': 'Action',
        'config_context': 'ConfigContext',
        'account': 'Account',
        'advanced_storage_config': 'AdvancedStorageConfig',
        'auto_support': 'AutoSupport',
        'config_result': 'ConfigResult',
        'data_ip_address': 'DataIpAddress',
        'ext_fc_storage': 'ExtFcStorage',
        'ext_iscsi_storage': 'ExtIscsiStorage',
        'hypervisor_type': 'HypervisorType',
        'local_credential': 'LocalCredential',
        'mac_address_prefix': 'MacAddressPrefix',
        'mgmt_ip_address': 'MgmtIpAddress',
        'mgmt_platform': 'MgmtPlatform',
        'network_config': 'NetworkConfig',
        'node_config': 'NodeConfig',
        'node_profile_config': 'NodeProfileConfig',
        'replication': 'Replication',
        'storage_data_vlan': 'StorageDataVlan',
        'sys_config': 'SysConfig',
        'ucsm_config': 'UcsmConfig',
        'vcenter_config': 'VcenterConfig'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, description=None, name=None, src_template=None, type='instance', action=None, config_context=None, account=None, advanced_storage_config=None, auto_support=None, config_result=None, data_ip_address=None, ext_fc_storage=None, ext_iscsi_storage=None, hypervisor_type='ESXi', local_credential=None, mac_address_prefix=None, mgmt_ip_address=None, mgmt_platform='FI', network_config=None, node_config=None, node_profile_config=None, replication=None, storage_data_vlan=None, sys_config=None, ucsm_config=None, vcenter_config=None):
        """
        HyperflexClusterProfile - a model defined in Swagger
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
        self._description = None
        self._name = None
        self._src_template = None
        self._type = None
        self._action = None
        self._config_context = None
        self._account = None
        self._advanced_storage_config = None
        self._auto_support = None
        self._config_result = None
        self._data_ip_address = None
        self._ext_fc_storage = None
        self._ext_iscsi_storage = None
        self._hypervisor_type = None
        self._local_credential = None
        self._mac_address_prefix = None
        self._mgmt_ip_address = None
        self._mgmt_platform = None
        self._network_config = None
        self._node_config = None
        self._node_profile_config = None
        self._replication = None
        self._storage_data_vlan = None
        self._sys_config = None
        self._ucsm_config = None
        self._vcenter_config = None

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
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if src_template is not None:
          self.src_template = src_template
        if type is not None:
          self.type = type
        if action is not None:
          self.action = action
        if config_context is not None:
          self.config_context = config_context
        if account is not None:
          self.account = account
        if advanced_storage_config is not None:
          self.advanced_storage_config = advanced_storage_config
        if auto_support is not None:
          self.auto_support = auto_support
        if config_result is not None:
          self.config_result = config_result
        if data_ip_address is not None:
          self.data_ip_address = data_ip_address
        if ext_fc_storage is not None:
          self.ext_fc_storage = ext_fc_storage
        if ext_iscsi_storage is not None:
          self.ext_iscsi_storage = ext_iscsi_storage
        if hypervisor_type is not None:
          self.hypervisor_type = hypervisor_type
        if local_credential is not None:
          self.local_credential = local_credential
        if mac_address_prefix is not None:
          self.mac_address_prefix = mac_address_prefix
        if mgmt_ip_address is not None:
          self.mgmt_ip_address = mgmt_ip_address
        if mgmt_platform is not None:
          self.mgmt_platform = mgmt_platform
        if network_config is not None:
          self.network_config = network_config
        if node_config is not None:
          self.node_config = node_config
        if node_profile_config is not None:
          self.node_profile_config = node_profile_config
        if replication is not None:
          self.replication = replication
        if storage_data_vlan is not None:
          self.storage_data_vlan = storage_data_vlan
        if sys_config is not None:
          self.sys_config = sys_config
        if ucsm_config is not None:
          self.ucsm_config = ucsm_config
        if vcenter_config is not None:
          self.vcenter_config = vcenter_config

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexClusterProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexClusterProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexClusterProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexClusterProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexClusterProfile.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexClusterProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexClusterProfile.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexClusterProfile.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexClusterProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexClusterProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexClusterProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexClusterProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexClusterProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexClusterProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexClusterProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexClusterProfile.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexClusterProfile.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexClusterProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexClusterProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexClusterProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexClusterProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexClusterProfile.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexClusterProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexClusterProfile.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexClusterProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexClusterProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexClusterProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexClusterProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this HyperflexClusterProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexClusterProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this HyperflexClusterProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def description(self):
        """
        Gets the description of this HyperflexClusterProfile.
        Description of the profile.  

        :return: The description of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexClusterProfile.
        Description of the profile.  

        :param description: The description of this HyperflexClusterProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexClusterProfile.
        Name of the profile.  

        :return: The name of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexClusterProfile.
        Name of the profile.  

        :param name: The name of this HyperflexClusterProfile.
        :type: str
        """

        self._name = name

    @property
    def src_template(self):
        """
        Gets the src_template of this HyperflexClusterProfile.

        :return: The src_template of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this HyperflexClusterProfile.

        :param src_template: The src_template of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._src_template = src_template

    @property
    def type(self):
        """
        Gets the type of this HyperflexClusterProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HyperflexClusterProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["instance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def action(self):
        """
        Gets the action of this HyperflexClusterProfile.
        User/system triggered action like \"NoOp\", \"Deploy\", \"Undeploy\", \"DryRun\", \"ComplianceCheck\", \"AnalyzeImpact\"  

        :return: The action of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this HyperflexClusterProfile.
        User/system triggered action like \"NoOp\", \"Deploy\", \"Undeploy\", \"DryRun\", \"ComplianceCheck\", \"AnalyzeImpact\"  

        :param action: The action of this HyperflexClusterProfile.
        :type: str
        """

        self._action = action

    @property
    def config_context(self):
        """
        Gets the config_context of this HyperflexClusterProfile.

        :return: The config_context of this HyperflexClusterProfile.
        :rtype: PolicyConfigContext
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """
        Sets the config_context of this HyperflexClusterProfile.

        :param config_context: The config_context of this HyperflexClusterProfile.
        :type: PolicyConfigContext
        """

        self._config_context = config_context

    @property
    def account(self):
        """
        Gets the account of this HyperflexClusterProfile.

        :return: The account of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this HyperflexClusterProfile.

        :param account: The account of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._account = account

    @property
    def advanced_storage_config(self):
        """
        Gets the advanced_storage_config of this HyperflexClusterProfile.

        :return: The advanced_storage_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._advanced_storage_config

    @advanced_storage_config.setter
    def advanced_storage_config(self, advanced_storage_config):
        """
        Sets the advanced_storage_config of this HyperflexClusterProfile.

        :param advanced_storage_config: The advanced_storage_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._advanced_storage_config = advanced_storage_config

    @property
    def auto_support(self):
        """
        Gets the auto_support of this HyperflexClusterProfile.

        :return: The auto_support of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._auto_support

    @auto_support.setter
    def auto_support(self, auto_support):
        """
        Sets the auto_support of this HyperflexClusterProfile.

        :param auto_support: The auto_support of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._auto_support = auto_support

    @property
    def config_result(self):
        """
        Gets the config_result of this HyperflexClusterProfile.

        :return: The config_result of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """
        Sets the config_result of this HyperflexClusterProfile.

        :param config_result: The config_result of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._config_result = config_result

    @property
    def data_ip_address(self):
        """
        Gets the data_ip_address of this HyperflexClusterProfile.
        Data IP address for the HyperFlex cluster  

        :return: The data_ip_address of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._data_ip_address

    @data_ip_address.setter
    def data_ip_address(self, data_ip_address):
        """
        Sets the data_ip_address of this HyperflexClusterProfile.
        Data IP address for the HyperFlex cluster  

        :param data_ip_address: The data_ip_address of this HyperflexClusterProfile.
        :type: str
        """

        self._data_ip_address = data_ip_address

    @property
    def ext_fc_storage(self):
        """
        Gets the ext_fc_storage of this HyperflexClusterProfile.

        :return: The ext_fc_storage of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._ext_fc_storage

    @ext_fc_storage.setter
    def ext_fc_storage(self, ext_fc_storage):
        """
        Sets the ext_fc_storage of this HyperflexClusterProfile.

        :param ext_fc_storage: The ext_fc_storage of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._ext_fc_storage = ext_fc_storage

    @property
    def ext_iscsi_storage(self):
        """
        Gets the ext_iscsi_storage of this HyperflexClusterProfile.

        :return: The ext_iscsi_storage of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._ext_iscsi_storage

    @ext_iscsi_storage.setter
    def ext_iscsi_storage(self, ext_iscsi_storage):
        """
        Sets the ext_iscsi_storage of this HyperflexClusterProfile.

        :param ext_iscsi_storage: The ext_iscsi_storage of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._ext_iscsi_storage = ext_iscsi_storage

    @property
    def hypervisor_type(self):
        """
        Gets the hypervisor_type of this HyperflexClusterProfile.
        Hypervisor Type for HyperFlex cluster  

        :return: The hypervisor_type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """
        Sets the hypervisor_type of this HyperflexClusterProfile.
        Hypervisor Type for HyperFlex cluster  

        :param hypervisor_type: The hypervisor_type of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["ESXi"]
        if hypervisor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `hypervisor_type` ({0}), must be one of {1}"
                .format(hypervisor_type, allowed_values)
            )

        self._hypervisor_type = hypervisor_type

    @property
    def local_credential(self):
        """
        Gets the local_credential of this HyperflexClusterProfile.

        :return: The local_credential of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._local_credential

    @local_credential.setter
    def local_credential(self, local_credential):
        """
        Sets the local_credential of this HyperflexClusterProfile.

        :param local_credential: The local_credential of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._local_credential = local_credential

    @property
    def mac_address_prefix(self):
        """
        Gets the mac_address_prefix of this HyperflexClusterProfile.

        :return: The mac_address_prefix of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mac_address_prefix

    @mac_address_prefix.setter
    def mac_address_prefix(self, mac_address_prefix):
        """
        Sets the mac_address_prefix of this HyperflexClusterProfile.

        :param mac_address_prefix: The mac_address_prefix of this HyperflexClusterProfile.
        :type: str
        """

        self._mac_address_prefix = mac_address_prefix

    @property
    def mgmt_ip_address(self):
        """
        Gets the mgmt_ip_address of this HyperflexClusterProfile.
        Management IP address for the HyperFlex cluster  

        :return: The mgmt_ip_address of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mgmt_ip_address

    @mgmt_ip_address.setter
    def mgmt_ip_address(self, mgmt_ip_address):
        """
        Sets the mgmt_ip_address of this HyperflexClusterProfile.
        Management IP address for the HyperFlex cluster  

        :param mgmt_ip_address: The mgmt_ip_address of this HyperflexClusterProfile.
        :type: str
        """

        self._mgmt_ip_address = mgmt_ip_address

    @property
    def mgmt_platform(self):
        """
        Gets the mgmt_platform of this HyperflexClusterProfile.
        Management platform for HyperFlex cluster  

        :return: The mgmt_platform of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mgmt_platform

    @mgmt_platform.setter
    def mgmt_platform(self, mgmt_platform):
        """
        Sets the mgmt_platform of this HyperflexClusterProfile.
        Management platform for HyperFlex cluster  

        :param mgmt_platform: The mgmt_platform of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["FI", "EDGE"]
        if mgmt_platform not in allowed_values:
            raise ValueError(
                "Invalid value for `mgmt_platform` ({0}), must be one of {1}"
                .format(mgmt_platform, allowed_values)
            )

        self._mgmt_platform = mgmt_platform

    @property
    def network_config(self):
        """
        Gets the network_config of this HyperflexClusterProfile.

        :return: The network_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        """
        Sets the network_config of this HyperflexClusterProfile.

        :param network_config: The network_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._network_config = network_config

    @property
    def node_config(self):
        """
        Gets the node_config of this HyperflexClusterProfile.

        :return: The node_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._node_config

    @node_config.setter
    def node_config(self, node_config):
        """
        Sets the node_config of this HyperflexClusterProfile.

        :param node_config: The node_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._node_config = node_config

    @property
    def node_profile_config(self):
        """
        Gets the node_profile_config of this HyperflexClusterProfile.

        :return: The node_profile_config of this HyperflexClusterProfile.
        :rtype: list[MoMoRef]
        """
        return self._node_profile_config

    @node_profile_config.setter
    def node_profile_config(self, node_profile_config):
        """
        Sets the node_profile_config of this HyperflexClusterProfile.

        :param node_profile_config: The node_profile_config of this HyperflexClusterProfile.
        :type: list[MoMoRef]
        """

        self._node_profile_config = node_profile_config

    @property
    def replication(self):
        """
        Gets the replication of this HyperflexClusterProfile.
        Defines the number of redundant replicas of data across the cluster  

        :return: The replication of this HyperflexClusterProfile.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """
        Sets the replication of this HyperflexClusterProfile.
        Defines the number of redundant replicas of data across the cluster  

        :param replication: The replication of this HyperflexClusterProfile.
        :type: int
        """

        self._replication = replication

    @property
    def storage_data_vlan(self):
        """
        Gets the storage_data_vlan of this HyperflexClusterProfile.
        VLAN for HyperFlex storage data traffic   

        :return: The storage_data_vlan of this HyperflexClusterProfile.
        :rtype: HyperflexNamedVlan
        """
        return self._storage_data_vlan

    @storage_data_vlan.setter
    def storage_data_vlan(self, storage_data_vlan):
        """
        Sets the storage_data_vlan of this HyperflexClusterProfile.
        VLAN for HyperFlex storage data traffic   

        :param storage_data_vlan: The storage_data_vlan of this HyperflexClusterProfile.
        :type: HyperflexNamedVlan
        """

        self._storage_data_vlan = storage_data_vlan

    @property
    def sys_config(self):
        """
        Gets the sys_config of this HyperflexClusterProfile.

        :return: The sys_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._sys_config

    @sys_config.setter
    def sys_config(self, sys_config):
        """
        Sets the sys_config of this HyperflexClusterProfile.

        :param sys_config: The sys_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._sys_config = sys_config

    @property
    def ucsm_config(self):
        """
        Gets the ucsm_config of this HyperflexClusterProfile.

        :return: The ucsm_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._ucsm_config

    @ucsm_config.setter
    def ucsm_config(self, ucsm_config):
        """
        Sets the ucsm_config of this HyperflexClusterProfile.

        :param ucsm_config: The ucsm_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._ucsm_config = ucsm_config

    @property
    def vcenter_config(self):
        """
        Gets the vcenter_config of this HyperflexClusterProfile.

        :return: The vcenter_config of this HyperflexClusterProfile.
        :rtype: MoMoRef
        """
        return self._vcenter_config

    @vcenter_config.setter
    def vcenter_config(self, vcenter_config):
        """
        Sets the vcenter_config of this HyperflexClusterProfile.

        :param vcenter_config: The vcenter_config of this HyperflexClusterProfile.
        :type: MoMoRef
        """

        self._vcenter_config = vcenter_config

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
        if not isinstance(other, HyperflexClusterProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
