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


class WorkflowCliCommandAllOf(object):
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
        'command': 'str',
        'end_prompt': 'str',
        'expect_prompts': 'list[WorkflowExpectPrompt]',
        'skip_status_check': 'bool',
        'terminal_end': 'bool',
        'terminal_start': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'command': 'Command',
        'end_prompt': 'EndPrompt',
        'expect_prompts': 'ExpectPrompts',
        'skip_status_check': 'SkipStatusCheck',
        'terminal_end': 'TerminalEnd',
        'terminal_start': 'TerminalStart',
        'type': 'Type'
    }

    def __init__(self,
                 command=None,
                 end_prompt=None,
                 expect_prompts=None,
                 skip_status_check=None,
                 terminal_end=None,
                 terminal_start=None,
                 type='NonInteractive',
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowCliCommandAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._command = None
        self._end_prompt = None
        self._expect_prompts = None
        self._skip_status_check = None
        self._terminal_end = None
        self._terminal_start = None
        self._type = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if end_prompt is not None:
            self.end_prompt = end_prompt
        if expect_prompts is not None:
            self.expect_prompts = expect_prompts
        if skip_status_check is not None:
            self.skip_status_check = skip_status_check
        if terminal_end is not None:
            self.terminal_end = terminal_end
        if terminal_start is not None:
            self.terminal_start = terminal_start
        if type is not None:
            self.type = type

    @property
    def command(self):
        """Gets the command of this WorkflowCliCommandAllOf.  # noqa: E501

        The command to run on the device connector.     # noqa: E501

        :return: The command of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this WorkflowCliCommandAllOf.

        The command to run on the device connector.     # noqa: E501

        :param command: The command of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def end_prompt(self):
        """Gets the end_prompt of this WorkflowCliCommandAllOf.  # noqa: E501

        The regex string that identifies the end of the command response.     # noqa: E501

        :return: The end_prompt of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: str
        """
        return self._end_prompt

    @end_prompt.setter
    def end_prompt(self, end_prompt):
        """Sets the end_prompt of this WorkflowCliCommandAllOf.

        The regex string that identifies the end of the command response.     # noqa: E501

        :param end_prompt: The end_prompt of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: str
        """

        self._end_prompt = end_prompt

    @property
    def expect_prompts(self):
        """Gets the expect_prompts of this WorkflowCliCommandAllOf.  # noqa: E501


        :return: The expect_prompts of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: list[WorkflowExpectPrompt]
        """
        return self._expect_prompts

    @expect_prompts.setter
    def expect_prompts(self, expect_prompts):
        """Sets the expect_prompts of this WorkflowCliCommandAllOf.


        :param expect_prompts: The expect_prompts of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: list[WorkflowExpectPrompt]
        """

        self._expect_prompts = expect_prompts

    @property
    def skip_status_check(self):
        """Gets the skip_status_check of this WorkflowCliCommandAllOf.  # noqa: E501

        Skips the execution status check of the terminal command. One use case for this is while exiting the terminal session from esxi host.     # noqa: E501

        :return: The skip_status_check of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._skip_status_check

    @skip_status_check.setter
    def skip_status_check(self, skip_status_check):
        """Sets the skip_status_check of this WorkflowCliCommandAllOf.

        Skips the execution status check of the terminal command. One use case for this is while exiting the terminal session from esxi host.     # noqa: E501

        :param skip_status_check: The skip_status_check of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: bool
        """

        self._skip_status_check = skip_status_check

    @property
    def terminal_end(self):
        """Gets the terminal_end of this WorkflowCliCommandAllOf.  # noqa: E501

        If this flag is set, it marks the end of the terminal session where the previous commands were executed.     # noqa: E501

        :return: The terminal_end of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._terminal_end

    @terminal_end.setter
    def terminal_end(self, terminal_end):
        """Sets the terminal_end of this WorkflowCliCommandAllOf.

        If this flag is set, it marks the end of the terminal session where the previous commands were executed.     # noqa: E501

        :param terminal_end: The terminal_end of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: bool
        """

        self._terminal_end = terminal_end

    @property
    def terminal_start(self):
        """Gets the terminal_start of this WorkflowCliCommandAllOf.  # noqa: E501

        If this flag is set, the execution of this command initiates a terminal session in which the subsequent CLI commands are executed until a command with terminalEnd flag is encountered or the end of the batch.     # noqa: E501

        :return: The terminal_start of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._terminal_start

    @terminal_start.setter
    def terminal_start(self, terminal_start):
        """Sets the terminal_start of this WorkflowCliCommandAllOf.

        If this flag is set, the execution of this command initiates a terminal session in which the subsequent CLI commands are executed until a command with terminalEnd flag is encountered or the end of the batch.     # noqa: E501

        :param terminal_start: The terminal_start of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: bool
        """

        self._terminal_start = terminal_start

    @property
    def type(self):
        """Gets the type of this WorkflowCliCommandAllOf.  # noqa: E501

        The type of the command - can be interactive or non-interactive.      # noqa: E501

        :return: The type of this WorkflowCliCommandAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkflowCliCommandAllOf.

        The type of the command - can be interactive or non-interactive.      # noqa: E501

        :param type: The type of this WorkflowCliCommandAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonInteractive", "Interactive"]  # noqa: E501
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
        if not isinstance(other, WorkflowCliCommandAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowCliCommandAllOf):
            return True

        return self.to_dict() != other.to_dict()
