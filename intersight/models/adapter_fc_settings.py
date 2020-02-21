# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1415
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AdapterFcSettings(object):
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
        'fip_enabled': 'bool'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'fip_enabled': 'FipEnabled'
    }

    def __init__(self, object_type=None, fip_enabled=None):
        """
        AdapterFcSettings - a model defined in Swagger
        """

        self._object_type = None
        self._fip_enabled = None

        if object_type is not None:
          self.object_type = object_type
        if fip_enabled is not None:
          self.fip_enabled = fip_enabled

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterFcSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this AdapterFcSettings.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterFcSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this AdapterFcSettings.
        :type: str
        """

        self._object_type = object_type

    @property
    def fip_enabled(self):
        """
        Gets the fip_enabled of this AdapterFcSettings.
        Status of FIP protocol on the adapter interfaces.   

        :return: The fip_enabled of this AdapterFcSettings.
        :rtype: bool
        """
        return self._fip_enabled

    @fip_enabled.setter
    def fip_enabled(self, fip_enabled):
        """
        Sets the fip_enabled of this AdapterFcSettings.
        Status of FIP protocol on the adapter interfaces.   

        :param fip_enabled: The fip_enabled of this AdapterFcSettings.
        :type: bool
        """

        self._fip_enabled = fip_enabled

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
        if not isinstance(other, AdapterFcSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
