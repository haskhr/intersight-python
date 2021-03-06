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


class ApplianceDataExportPolicyAllOf(object):
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
        'enable': 'bool',
        'name': 'str',
        'account': 'IamAccount',
        'parent_config': 'ApplianceDataExportPolicy',
        'sub_configs': 'list[ApplianceDataExportPolicy]'
    }

    attribute_map = {
        'enable': 'Enable',
        'name': 'Name',
        'account': 'Account',
        'parent_config': 'ParentConfig',
        'sub_configs': 'SubConfigs'
    }

    def __init__(self,
                 enable=None,
                 name=None,
                 account=None,
                 parent_config=None,
                 sub_configs=None,
                 local_vars_configuration=None):  # noqa: E501
        """ApplianceDataExportPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable = None
        self._name = None
        self._account = None
        self._parent_config = None
        self._sub_configs = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if name is not None:
            self.name = name
        if account is not None:
            self.account = account
        if parent_config is not None:
            self.parent_config = parent_config
        if sub_configs is not None:
            self.sub_configs = sub_configs

    @property
    def enable(self):
        """Gets the enable of this ApplianceDataExportPolicyAllOf.  # noqa: E501

        Status of the data collection mode. If the value is 'true', then data collection is enabled.    # noqa: E501

        :return: The enable of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ApplianceDataExportPolicyAllOf.

        Status of the data collection mode. If the value is 'true', then data collection is enabled.    # noqa: E501

        :param enable: The enable of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def name(self):
        """Gets the name of this ApplianceDataExportPolicyAllOf.  # noqa: E501

        Name of the Data Export Policy.     # noqa: E501

        :return: The name of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplianceDataExportPolicyAllOf.

        Name of the Data Export Policy.     # noqa: E501

        :param name: The name of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account(self):
        """Gets the account of this ApplianceDataExportPolicyAllOf.  # noqa: E501


        :return: The account of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ApplianceDataExportPolicyAllOf.


        :param account: The account of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def parent_config(self):
        """Gets the parent_config of this ApplianceDataExportPolicyAllOf.  # noqa: E501


        :return: The parent_config of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :rtype: ApplianceDataExportPolicy
        """
        return self._parent_config

    @parent_config.setter
    def parent_config(self, parent_config):
        """Sets the parent_config of this ApplianceDataExportPolicyAllOf.


        :param parent_config: The parent_config of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :type: ApplianceDataExportPolicy
        """

        self._parent_config = parent_config

    @property
    def sub_configs(self):
        """Gets the sub_configs of this ApplianceDataExportPolicyAllOf.  # noqa: E501

        A reference to a applianceDataExportPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Sub-configurations of the current Data Export Policy. For example, if the current Data Export Policy is Inventory, the sub-configurations would include the Network and Storage inventory.   # noqa: E501

        :return: The sub_configs of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :rtype: list[ApplianceDataExportPolicy]
        """
        return self._sub_configs

    @sub_configs.setter
    def sub_configs(self, sub_configs):
        """Sets the sub_configs of this ApplianceDataExportPolicyAllOf.

        A reference to a applianceDataExportPolicy resource. When the $expand query parameter is specified, the referenced resource is returned inline. Sub-configurations of the current Data Export Policy. For example, if the current Data Export Policy is Inventory, the sub-configurations would include the Network and Storage inventory.   # noqa: E501

        :param sub_configs: The sub_configs of this ApplianceDataExportPolicyAllOf.  # noqa: E501
        :type: list[ApplianceDataExportPolicy]
        """

        self._sub_configs = sub_configs

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
        if not isinstance(other, ApplianceDataExportPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceDataExportPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
