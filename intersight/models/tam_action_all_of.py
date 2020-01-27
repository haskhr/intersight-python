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


class TamActionAllOf(object):
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
        'affected_object_type': 'str',
        'alert_type': 'str',
        'identifiers': 'list[TamIdentifiers]',
        'name': 'str',
        'operation_type': 'str',
        'queries': 'list[TamQueryEntry]',
        'type': 'str'
    }

    attribute_map = {
        'affected_object_type': 'AffectedObjectType',
        'alert_type': 'AlertType',
        'identifiers': 'Identifiers',
        'name': 'Name',
        'operation_type': 'OperationType',
        'queries': 'Queries',
        'type': 'Type'
    }

    def __init__(self,
                 affected_object_type=None,
                 alert_type='psirt',
                 identifiers=None,
                 name=None,
                 operation_type='create',
                 queries=None,
                 type='restApi',
                 local_vars_configuration=None):  # noqa: E501
        """TamActionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affected_object_type = None
        self._alert_type = None
        self._identifiers = None
        self._name = None
        self._operation_type = None
        self._queries = None
        self._type = None
        self.discriminator = None

        if affected_object_type is not None:
            self.affected_object_type = affected_object_type
        if alert_type is not None:
            self.alert_type = alert_type
        if identifiers is not None:
            self.identifiers = identifiers
        if name is not None:
            self.name = name
        if operation_type is not None:
            self.operation_type = operation_type
        if queries is not None:
            self.queries = queries
        if type is not None:
            self.type = type

    @property
    def affected_object_type(self):
        """Gets the affected_object_type of this TamActionAllOf.  # noqa: E501

        Type of the managed object that should be marked with an instance of the Alert (when operation type is create) or that should have an alert instance removed (when operation type is remove).    # noqa: E501

        :return: The affected_object_type of this TamActionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._affected_object_type

    @affected_object_type.setter
    def affected_object_type(self, affected_object_type):
        """Sets the affected_object_type of this TamActionAllOf.

        Type of the managed object that should be marked with an instance of the Alert (when operation type is create) or that should have an alert instance removed (when operation type is remove).    # noqa: E501

        :param affected_object_type: The affected_object_type of this TamActionAllOf.  # noqa: E501
        :type: str
        """

        self._affected_object_type = affected_object_type

    @property
    def alert_type(self):
        """Gets the alert_type of this TamActionAllOf.  # noqa: E501

        Alert type is used to denote the category of an Intersight alert (FieldNotice, equipment Fault etc.).    # noqa: E501

        :return: The alert_type of this TamActionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this TamActionAllOf.

        Alert type is used to denote the category of an Intersight alert (FieldNotice, equipment Fault etc.).    # noqa: E501

        :param alert_type: The alert_type of this TamActionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["psirt", "fieldNotice"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and alert_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `alert_type` ({0}), must be one of {1}"  # noqa: E501
                .format(alert_type, allowed_values))

        self._alert_type = alert_type

    @property
    def identifiers(self):
        """Gets the identifiers of this TamActionAllOf.  # noqa: E501


        :return: The identifiers of this TamActionAllOf.  # noqa: E501
        :rtype: list[TamIdentifiers]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this TamActionAllOf.


        :param identifiers: The identifiers of this TamActionAllOf.  # noqa: E501
        :type: list[TamIdentifiers]
        """

        self._identifiers = identifiers

    @property
    def name(self):
        """Gets the name of this TamActionAllOf.  # noqa: E501

        Uniquely identifies a given action among the set of actions corresponding to an advisory. Primarily used to store and compare results of subsequent iterations corresponding to the action queries.    # noqa: E501

        :return: The name of this TamActionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TamActionAllOf.

        Uniquely identifies a given action among the set of actions corresponding to an advisory. Primarily used to store and compare results of subsequent iterations corresponding to the action queries.    # noqa: E501

        :param name: The name of this TamActionAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def operation_type(self):
        """Gets the operation_type of this TamActionAllOf.  # noqa: E501

        Operation type for the alert action. An action is used to carry out the process of \"reacting\" to an alert condition. For e.g.in case of a fieldNotice alert, the intention may be to create a new alert (if the condition matches and there is no existing alert) or to remove an existing alert when the alert condition has been remedied.    # noqa: E501

        :return: The operation_type of this TamActionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this TamActionAllOf.

        Operation type for the alert action. An action is used to carry out the process of \"reacting\" to an alert condition. For e.g.in case of a fieldNotice alert, the intention may be to create a new alert (if the condition matches and there is no existing alert) or to remove an existing alert when the alert condition has been remedied.    # noqa: E501

        :param operation_type: The operation_type of this TamActionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["create", "remove"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operation_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_type, allowed_values))

        self._operation_type = operation_type

    @property
    def queries(self):
        """Gets the queries of this TamActionAllOf.  # noqa: E501


        :return: The queries of this TamActionAllOf.  # noqa: E501
        :rtype: list[TamQueryEntry]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this TamActionAllOf.


        :param queries: The queries of this TamActionAllOf.  # noqa: E501
        :type: list[TamQueryEntry]
        """

        self._queries = queries

    @property
    def type(self):
        """Gets the type of this TamActionAllOf.  # noqa: E501

        Type of Intersight alert. An alert in Intersight could be one of several kinds (FieldNotice, PSIRT etc.). Primarily used for filtering alerts based on the type.     # noqa: E501

        :return: The type of this TamActionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TamActionAllOf.

        Type of Intersight alert. An alert in Intersight could be one of several kinds (FieldNotice, PSIRT etc.). Primarily used for filtering alerts based on the type.     # noqa: E501

        :param type: The type of this TamActionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["restApi"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

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
        if not isinstance(other, TamActionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TamActionAllOf):
            return True

        return self.to_dict() != other.to_dict()