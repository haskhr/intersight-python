# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.7-681
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IamAccountPermissions(object):
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
        'account_identifier': 'str',
        'account_name': 'str',
        'account_status': 'str',
        'permissions': 'list[IamPermissionReference]'
    }

    attribute_map = {
        'account_identifier': 'AccountIdentifier',
        'account_name': 'AccountName',
        'account_status': 'AccountStatus',
        'permissions': 'Permissions'
    }

    def __init__(self, account_identifier=None, account_name=None, account_status=None, permissions=None):
        """
        IamAccountPermissions - a model defined in Swagger
        """

        self._account_identifier = None
        self._account_name = None
        self._account_status = None
        self._permissions = None

        if account_identifier is not None:
          self.account_identifier = account_identifier
        if account_name is not None:
          self.account_name = account_name
        if account_status is not None:
          self.account_status = account_status
        if permissions is not None:
          self.permissions = permissions

    @property
    def account_identifier(self):
        """
        Gets the account_identifier of this IamAccountPermissions.
        MOID of the account which a user can select after authentication.  

        :return: The account_identifier of this IamAccountPermissions.
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """
        Sets the account_identifier of this IamAccountPermissions.
        MOID of the account which a user can select after authentication.  

        :param account_identifier: The account_identifier of this IamAccountPermissions.
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def account_name(self):
        """
        Gets the account_name of this IamAccountPermissions.
        Name of the account which a user can select after authentication.  

        :return: The account_name of this IamAccountPermissions.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this IamAccountPermissions.
        Name of the account which a user can select after authentication.  

        :param account_name: The account_name of this IamAccountPermissions.
        :type: str
        """

        self._account_name = account_name

    @property
    def account_status(self):
        """
        Gets the account_status of this IamAccountPermissions.
        Status of the account. Account remains inactive until a device is claimed to the account.  

        :return: The account_status of this IamAccountPermissions.
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """
        Sets the account_status of this IamAccountPermissions.
        Status of the account. Account remains inactive until a device is claimed to the account.  

        :param account_status: The account_status of this IamAccountPermissions.
        :type: str
        """

        self._account_status = account_status

    @property
    def permissions(self):
        """
        Gets the permissions of this IamAccountPermissions.
        Permissions within an account which a user can select after authentication.   

        :return: The permissions of this IamAccountPermissions.
        :rtype: list[IamPermissionReference]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this IamAccountPermissions.
        Permissions within an account which a user can select after authentication.   

        :param permissions: The permissions of this IamAccountPermissions.
        :type: list[IamPermissionReference]
        """

        self._permissions = permissions

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
        if not isinstance(other, IamAccountPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
