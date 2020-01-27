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


class MemoryAbstractUnit(object):
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
        'admin_state': 'str',
        'array_id': 'int',
        'bank': 'int',
        'capacity': 'str',
        'clock': 'str',
        'form_factor': 'str',
        'latency': 'str',
        'location': 'str',
        'oper_power_state': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'set': 'int',
        'speed': 'str',
        'thermal': 'str',
        'type': 'str',
        'visibility': 'str',
        'width': 'str'
    }

    attribute_map = {
        'admin_state': 'AdminState',
        'array_id': 'ArrayId',
        'bank': 'Bank',
        'capacity': 'Capacity',
        'clock': 'Clock',
        'form_factor': 'FormFactor',
        'latency': 'Latency',
        'location': 'Location',
        'oper_power_state': 'OperPowerState',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'set': 'Set',
        'speed': 'Speed',
        'thermal': 'Thermal',
        'type': 'Type',
        'visibility': 'Visibility',
        'width': 'Width'
    }

    def __init__(self,
                 admin_state=None,
                 array_id=None,
                 bank=None,
                 capacity=None,
                 clock=None,
                 form_factor=None,
                 latency=None,
                 location=None,
                 oper_power_state=None,
                 oper_state=None,
                 operability=None,
                 presence=None,
                 set=None,
                 speed=None,
                 thermal=None,
                 type=None,
                 visibility=None,
                 width=None,
                 local_vars_configuration=None):  # noqa: E501
        """MemoryAbstractUnit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_state = None
        self._array_id = None
        self._bank = None
        self._capacity = None
        self._clock = None
        self._form_factor = None
        self._latency = None
        self._location = None
        self._oper_power_state = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._set = None
        self._speed = None
        self._thermal = None
        self._type = None
        self._visibility = None
        self._width = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if array_id is not None:
            self.array_id = array_id
        if bank is not None:
            self.bank = bank
        if capacity is not None:
            self.capacity = capacity
        if clock is not None:
            self.clock = clock
        if form_factor is not None:
            self.form_factor = form_factor
        if latency is not None:
            self.latency = latency
        if location is not None:
            self.location = location
        if oper_power_state is not None:
            self.oper_power_state = oper_power_state
        if oper_state is not None:
            self.oper_state = oper_state
        if operability is not None:
            self.operability = operability
        if presence is not None:
            self.presence = presence
        if set is not None:
            self.set = set
        if speed is not None:
            self.speed = speed
        if thermal is not None:
            self.thermal = thermal
        if type is not None:
            self.type = type
        if visibility is not None:
            self.visibility = visibility
        if width is not None:
            self.width = width

    @property
    def admin_state(self):
        """Gets the admin_state of this MemoryAbstractUnit.  # noqa: E501

        This represents the administrative state of the memory unit on a server.    # noqa: E501

        :return: The admin_state of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this MemoryAbstractUnit.

        This represents the administrative state of the memory unit on a server.    # noqa: E501

        :param admin_state: The admin_state of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._admin_state = admin_state

    @property
    def array_id(self):
        """Gets the array_id of this MemoryAbstractUnit.  # noqa: E501

        This represents the memory array to which the memory unit belongs to.    # noqa: E501

        :return: The array_id of this MemoryAbstractUnit.  # noqa: E501
        :rtype: int
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """Sets the array_id of this MemoryAbstractUnit.

        This represents the memory array to which the memory unit belongs to.    # noqa: E501

        :param array_id: The array_id of this MemoryAbstractUnit.  # noqa: E501
        :type: int
        """

        self._array_id = array_id

    @property
    def bank(self):
        """Gets the bank of this MemoryAbstractUnit.  # noqa: E501

        This represents the memory bank of the memory unit on a server.    # noqa: E501

        :return: The bank of this MemoryAbstractUnit.  # noqa: E501
        :rtype: int
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this MemoryAbstractUnit.

        This represents the memory bank of the memory unit on a server.    # noqa: E501

        :param bank: The bank of this MemoryAbstractUnit.  # noqa: E501
        :type: int
        """

        self._bank = bank

    @property
    def capacity(self):
        """Gets the capacity of this MemoryAbstractUnit.  # noqa: E501

        This represents the memory capacity in MiB of the memory unit on a server.    # noqa: E501

        :return: The capacity of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this MemoryAbstractUnit.

        This represents the memory capacity in MiB of the memory unit on a server.    # noqa: E501

        :param capacity: The capacity of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def clock(self):
        """Gets the clock of this MemoryAbstractUnit.  # noqa: E501

        This represents the clock of the memory unit on a server.    # noqa: E501

        :return: The clock of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this MemoryAbstractUnit.

        This represents the clock of the memory unit on a server.    # noqa: E501

        :param clock: The clock of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._clock = clock

    @property
    def form_factor(self):
        """Gets the form_factor of this MemoryAbstractUnit.  # noqa: E501

        This represents the form factor of the memory unit on a server.    # noqa: E501

        :return: The form_factor of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """Sets the form_factor of this MemoryAbstractUnit.

        This represents the form factor of the memory unit on a server.    # noqa: E501

        :param form_factor: The form_factor of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._form_factor = form_factor

    @property
    def latency(self):
        """Gets the latency of this MemoryAbstractUnit.  # noqa: E501

        This represents the latency of the memory unit on a server.    # noqa: E501

        :return: The latency of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this MemoryAbstractUnit.

        This represents the latency of the memory unit on a server.    # noqa: E501

        :param latency: The latency of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._latency = latency

    @property
    def location(self):
        """Gets the location of this MemoryAbstractUnit.  # noqa: E501

        This represents the location of the memory unit on a server.    # noqa: E501

        :return: The location of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MemoryAbstractUnit.

        This represents the location of the memory unit on a server.    # noqa: E501

        :param location: The location of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def oper_power_state(self):
        """Gets the oper_power_state of this MemoryAbstractUnit.  # noqa: E501

        This represents the operational power state of the memory unit on a server.    # noqa: E501

        :return: The oper_power_state of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """Sets the oper_power_state of this MemoryAbstractUnit.

        This represents the operational power state of the memory unit on a server.    # noqa: E501

        :param oper_power_state: The oper_power_state of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def oper_state(self):
        """Gets the oper_state of this MemoryAbstractUnit.  # noqa: E501

        This represents the operational state of the memory unit on a server.    # noqa: E501

        :return: The oper_state of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this MemoryAbstractUnit.

        This represents the operational state of the memory unit on a server.    # noqa: E501

        :param oper_state: The oper_state of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """Gets the operability of this MemoryAbstractUnit.  # noqa: E501

        This represents the operability of the memory unit on a server.    # noqa: E501

        :return: The operability of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """Sets the operability of this MemoryAbstractUnit.

        This represents the operability of the memory unit on a server.    # noqa: E501

        :param operability: The operability of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._operability = operability

    @property
    def presence(self):
        """Gets the presence of this MemoryAbstractUnit.  # noqa: E501

        This represents the presence state of the memory unit on a server.    # noqa: E501

        :return: The presence of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this MemoryAbstractUnit.

        This represents the presence state of the memory unit on a server.    # noqa: E501

        :param presence: The presence of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def set(self):
        """Gets the set of this MemoryAbstractUnit.  # noqa: E501

        This represents the set of the memory unit on a server.    # noqa: E501

        :return: The set of this MemoryAbstractUnit.  # noqa: E501
        :rtype: int
        """
        return self._set

    @set.setter
    def set(self, set):
        """Sets the set of this MemoryAbstractUnit.

        This represents the set of the memory unit on a server.    # noqa: E501

        :param set: The set of this MemoryAbstractUnit.  # noqa: E501
        :type: int
        """

        self._set = set

    @property
    def speed(self):
        """Gets the speed of this MemoryAbstractUnit.  # noqa: E501

        This represents the speed of the memory unit on a server.    # noqa: E501

        :return: The speed of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this MemoryAbstractUnit.

        This represents the speed of the memory unit on a server.    # noqa: E501

        :param speed: The speed of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._speed = speed

    @property
    def thermal(self):
        """Gets the thermal of this MemoryAbstractUnit.  # noqa: E501

        This represents the thremal state of the memory unit on a server.    # noqa: E501

        :return: The thermal of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """Sets the thermal of this MemoryAbstractUnit.

        This represents the thremal state of the memory unit on a server.    # noqa: E501

        :param thermal: The thermal of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._thermal = thermal

    @property
    def type(self):
        """Gets the type of this MemoryAbstractUnit.  # noqa: E501

        This represents the memory type of the memory unit on a server.    # noqa: E501

        :return: The type of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MemoryAbstractUnit.

        This represents the memory type of the memory unit on a server.    # noqa: E501

        :param type: The type of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def visibility(self):
        """Gets the visibility of this MemoryAbstractUnit.  # noqa: E501

        This represents the visibility of the memory unit on a server.    # noqa: E501

        :return: The visibility of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this MemoryAbstractUnit.

        This represents the visibility of the memory unit on a server.    # noqa: E501

        :param visibility: The visibility of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def width(self):
        """Gets the width of this MemoryAbstractUnit.  # noqa: E501

        This represents the width of the memory unit on a server.     # noqa: E501

        :return: The width of this MemoryAbstractUnit.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MemoryAbstractUnit.

        This represents the width of the memory unit on a server.     # noqa: E501

        :param width: The width of this MemoryAbstractUnit.  # noqa: E501
        :type: str
        """

        self._width = width

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
        if not isinstance(other, MemoryAbstractUnit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemoryAbstractUnit):
            return True

        return self.to_dict() != other.to_dict()