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


class AssetProductInformationAllOf(object):
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
        'bill_to': 'AssetAddressInformation',
        'description': 'str',
        'family': 'str',
        'group': 'str',
        'number': 'str',
        'ship_to': 'AssetAddressInformation',
        'sub_type': 'str'
    }

    attribute_map = {
        'bill_to': 'BillTo',
        'description': 'Description',
        'family': 'Family',
        'group': 'Group',
        'number': 'Number',
        'ship_to': 'ShipTo',
        'sub_type': 'SubType'
    }

    def __init__(self,
                 bill_to=None,
                 description=None,
                 family=None,
                 group=None,
                 number=None,
                 ship_to=None,
                 sub_type=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetProductInformationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bill_to = None
        self._description = None
        self._family = None
        self._group = None
        self._number = None
        self._ship_to = None
        self._sub_type = None
        self.discriminator = None

        if bill_to is not None:
            self.bill_to = bill_to
        if description is not None:
            self.description = description
        if family is not None:
            self.family = family
        if group is not None:
            self.group = group
        if number is not None:
            self.number = number
        if ship_to is not None:
            self.ship_to = ship_to
        if sub_type is not None:
            self.sub_type = sub_type

    @property
    def bill_to(self):
        """Gets the bill_to of this AssetProductInformationAllOf.  # noqa: E501


        :return: The bill_to of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: AssetAddressInformation
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """Sets the bill_to of this AssetProductInformationAllOf.


        :param bill_to: The bill_to of this AssetProductInformationAllOf.  # noqa: E501
        :type: AssetAddressInformation
        """

        self._bill_to = bill_to

    @property
    def description(self):
        """Gets the description of this AssetProductInformationAllOf.  # noqa: E501

        Short description of the Cisco product that helps identify the product easily. example \"DISTI:UCS 6248UP 1RU Fabric Int/No PSU/32 UP/ 12p LIC\".    # noqa: E501

        :return: The description of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetProductInformationAllOf.

        Short description of the Cisco product that helps identify the product easily. example \"DISTI:UCS 6248UP 1RU Fabric Int/No PSU/32 UP/ 12p LIC\".    # noqa: E501

        :param description: The description of this AssetProductInformationAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def family(self):
        """Gets the family of this AssetProductInformationAllOf.  # noqa: E501

        Family that the product belongs to. Example \"UCSB\".    # noqa: E501

        :return: The family of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this AssetProductInformationAllOf.

        Family that the product belongs to. Example \"UCSB\".    # noqa: E501

        :param family: The family of this AssetProductInformationAllOf.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def group(self):
        """Gets the group of this AssetProductInformationAllOf.  # noqa: E501

        Group that the product belongs to. It is one higher level categorization above family. example \"Switch\".    # noqa: E501

        :return: The group of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AssetProductInformationAllOf.

        Group that the product belongs to. It is one higher level categorization above family. example \"Switch\".    # noqa: E501

        :param group: The group of this AssetProductInformationAllOf.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def number(self):
        """Gets the number of this AssetProductInformationAllOf.  # noqa: E501

        Product number that identifies the product. example PID. example \"UCS-FI-6248UP-CH2\".    # noqa: E501

        :return: The number of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AssetProductInformationAllOf.

        Product number that identifies the product. example PID. example \"UCS-FI-6248UP-CH2\".    # noqa: E501

        :param number: The number of this AssetProductInformationAllOf.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def ship_to(self):
        """Gets the ship_to of this AssetProductInformationAllOf.  # noqa: E501


        :return: The ship_to of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: AssetAddressInformation
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this AssetProductInformationAllOf.


        :param ship_to: The ship_to of this AssetProductInformationAllOf.  # noqa: E501
        :type: AssetAddressInformation
        """

        self._ship_to = ship_to

    @property
    def sub_type(self):
        """Gets the sub_type of this AssetProductInformationAllOf.  # noqa: E501

        Sub type of the product being specified. example \"UCS 6200 SER\".     # noqa: E501

        :return: The sub_type of this AssetProductInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this AssetProductInformationAllOf.

        Sub type of the product being specified. example \"UCS 6200 SER\".     # noqa: E501

        :param sub_type: The sub_type of this AssetProductInformationAllOf.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

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
        if not isinstance(other, AssetProductInformationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetProductInformationAllOf):
            return True

        return self.to_dict() != other.to_dict()
