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


class TamAdvisoryAllOf(object):
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
        'description': 'str',
        'name': 'str',
        'severity': 'TamSeverity',
        'state': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'name': 'Name',
        'severity': 'Severity',
        'state': 'State'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 severity=None,
                 state='active',
                 local_vars_configuration=None):  # noqa: E501
        """TamAdvisoryAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._severity = None
        self._state = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state

    @property
    def description(self):
        """Gets the description of this TamAdvisoryAllOf.  # noqa: E501

        Brief description of the advisory details.    # noqa: E501

        :return: The description of this TamAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TamAdvisoryAllOf.

        Brief description of the advisory details.    # noqa: E501

        :param description: The description of this TamAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this TamAdvisoryAllOf.  # noqa: E501

        A user defined name for the Intersight Advisory.    # noqa: E501

        :return: The name of this TamAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TamAdvisoryAllOf.

        A user defined name for the Intersight Advisory.    # noqa: E501

        :param name: The name of this TamAdvisoryAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def severity(self):
        """Gets the severity of this TamAdvisoryAllOf.  # noqa: E501


        :return: The severity of this TamAdvisoryAllOf.  # noqa: E501
        :rtype: TamSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this TamAdvisoryAllOf.


        :param severity: The severity of this TamAdvisoryAllOf.  # noqa: E501
        :type: TamSeverity
        """

        self._severity = severity

    @property
    def state(self):
        """Gets the state of this TamAdvisoryAllOf.  # noqa: E501

        Current state of the advisory. Indicates if the user is interested in getting updates for the advisory.     # noqa: E501

        :return: The state of this TamAdvisoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TamAdvisoryAllOf.

        Current state of the advisory. Indicates if the user is interested in getting updates for the advisory.     # noqa: E501

        :param state: The state of this TamAdvisoryAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "acknowledged"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values))

        self._state = state

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
        if not isinstance(other, TamAdvisoryAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TamAdvisoryAllOf):
            return True

        return self.to_dict() != other.to_dict()