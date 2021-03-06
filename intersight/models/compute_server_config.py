# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComputeServerConfig(object):
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
        'object_type': 'str',
        'asset_tag': 'str',
        'user_label': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'asset_tag': 'AssetTag',
        'user_label': 'UserLabel'
    }

    def __init__(self, object_type=None, asset_tag=None, user_label=None):
        """
        ComputeServerConfig - a model defined in Swagger
        """

        self._object_type = None
        self._asset_tag = None
        self._user_label = None

        if object_type is not None:
          self.object_type = object_type
        if asset_tag is not None:
          self.asset_tag = asset_tag
        if user_label is not None:
          self.user_label = user_label

    @property
    def object_type(self):
        """
        Gets the object_type of this ComputeServerConfig.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this ComputeServerConfig.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ComputeServerConfig.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this ComputeServerConfig.
        :type: str
        """

        self._object_type = object_type

    @property
    def asset_tag(self):
        """
        Gets the asset_tag of this ComputeServerConfig.
        User defined asset tag of the server.

        :return: The asset_tag of this ComputeServerConfig.
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """
        Sets the asset_tag of this ComputeServerConfig.
        User defined asset tag of the server.

        :param asset_tag: The asset_tag of this ComputeServerConfig.
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def user_label(self):
        """
        Gets the user_label of this ComputeServerConfig.
        User defined description of the server.

        :return: The user_label of this ComputeServerConfig.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """
        Sets the user_label of this ComputeServerConfig.
        User defined description of the server.

        :param user_label: The user_label of this ComputeServerConfig.
        :type: str
        """

        self._user_label = user_label

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
        if not isinstance(other, ComputeServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
