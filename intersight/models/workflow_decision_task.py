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


class WorkflowDecisionTask(object):
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
        'condition': 'str',
        'decision_cases': 'list[WorkflowDecisionCase]',
        'default_task': 'str',
        'input_parameters': 'object'
    }

    attribute_map = {
        'condition': 'Condition',
        'decision_cases': 'DecisionCases',
        'default_task': 'DefaultTask',
        'input_parameters': 'InputParameters'
    }

    def __init__(self,
                 condition=None,
                 decision_cases=None,
                 default_task=None,
                 input_parameters=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowDecisionTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._condition = None
        self._decision_cases = None
        self._default_task = None
        self._input_parameters = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if decision_cases is not None:
            self.decision_cases = decision_cases
        if default_task is not None:
            self.default_task = default_task
        if input_parameters is not None:
            self.input_parameters = input_parameters

    @property
    def condition(self):
        """Gets the condition of this WorkflowDecisionTask.  # noqa: E501

        The condition to evaluate for this decision task. The condition can be a workflow or task variable or an expression based on the input parameters. Example value for condition if its Workflow/task variable is -  \"${task1.output.var1} or ${workflow.input.var2}\" which evaluates to a value matching any of the decision case values. Example value for condition if its an expression is - \"if ( $.element ! = null && $.element > 0 ) 'true'; else 'false'; \" which evaluates to 'true' or 'false' and will match one of the decision case values. Here \"element\" is a variable in decisiontask's inputParameters JSON formatted map. You can also use javascript like functions indexOf, toUpperCase in the expression which will be evaluated by the expression evaluator.    # noqa: E501

        :return: The condition of this WorkflowDecisionTask.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this WorkflowDecisionTask.

        The condition to evaluate for this decision task. The condition can be a workflow or task variable or an expression based on the input parameters. Example value for condition if its Workflow/task variable is -  \"${task1.output.var1} or ${workflow.input.var2}\" which evaluates to a value matching any of the decision case values. Example value for condition if its an expression is - \"if ( $.element ! = null && $.element > 0 ) 'true'; else 'false'; \" which evaluates to 'true' or 'false' and will match one of the decision case values. Here \"element\" is a variable in decisiontask's inputParameters JSON formatted map. You can also use javascript like functions indexOf, toUpperCase in the expression which will be evaluated by the expression evaluator.    # noqa: E501

        :param condition: The condition of this WorkflowDecisionTask.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def decision_cases(self):
        """Gets the decision_cases of this WorkflowDecisionTask.  # noqa: E501


        :return: The decision_cases of this WorkflowDecisionTask.  # noqa: E501
        :rtype: list[WorkflowDecisionCase]
        """
        return self._decision_cases

    @decision_cases.setter
    def decision_cases(self, decision_cases):
        """Sets the decision_cases of this WorkflowDecisionTask.


        :param decision_cases: The decision_cases of this WorkflowDecisionTask.  # noqa: E501
        :type: list[WorkflowDecisionCase]
        """

        self._decision_cases = decision_cases

    @property
    def default_task(self):
        """Gets the default_task of this WorkflowDecisionTask.  # noqa: E501

        The default next Task to execute if the decision cannot be evaluated to any of the DecisionCases.    # noqa: E501

        :return: The default_task of this WorkflowDecisionTask.  # noqa: E501
        :rtype: str
        """
        return self._default_task

    @default_task.setter
    def default_task(self, default_task):
        """Sets the default_task of this WorkflowDecisionTask.

        The default next Task to execute if the decision cannot be evaluated to any of the DecisionCases.    # noqa: E501

        :param default_task: The default_task of this WorkflowDecisionTask.  # noqa: E501
        :type: str
        """

        self._default_task = default_task

    @property
    def input_parameters(self):
        """Gets the input_parameters of this WorkflowDecisionTask.  # noqa: E501

        JSON formatted map that defines the input given to the decision task. The inputs are used as variables in the condition property of decision task. The input variables can be static values like \"hello\" , \"24\", \"true\" OR previous task outputs/workflow inputs like \"${task2.output.var1}}\". The input variables are referrenced as $.inputVariableName in the condition property.     # noqa: E501

        :return: The input_parameters of this WorkflowDecisionTask.  # noqa: E501
        :rtype: object
        """
        return self._input_parameters

    @input_parameters.setter
    def input_parameters(self, input_parameters):
        """Sets the input_parameters of this WorkflowDecisionTask.

        JSON formatted map that defines the input given to the decision task. The inputs are used as variables in the condition property of decision task. The input variables can be static values like \"hello\" , \"24\", \"true\" OR previous task outputs/workflow inputs like \"${task2.output.var1}}\". The input variables are referrenced as $.inputVariableName in the condition property.     # noqa: E501

        :param input_parameters: The input_parameters of this WorkflowDecisionTask.  # noqa: E501
        :type: object
        """

        self._input_parameters = input_parameters

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
        if not isinstance(other, WorkflowDecisionTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowDecisionTask):
            return True

        return self.to_dict() != other.to_dict()