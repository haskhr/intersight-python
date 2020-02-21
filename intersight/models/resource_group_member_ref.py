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


class ResourceGroupMemberRef(object):
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
        'moid': 'str',
        'selector': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'moid': 'Moid',
        'selector': 'Selector'
    }

    def __init__(self, object_type=None, moid=None, selector=None):
        """
        ResourceGroupMemberRef - a model defined in Swagger
        """

        self._object_type = None
        self._moid = None
        self._selector = None

        if object_type is not None:
          self.object_type = object_type
        if moid is not None:
          self.moid = moid
        if selector is not None:
          self.selector = selector

    @property
    def object_type(self):
        """
        Gets the object_type of this ResourceGroupMemberRef.
        The Object Type of the referenced REST resource.  

        :return: The object_type of this ResourceGroupMemberRef.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ResourceGroupMemberRef.
        The Object Type of the referenced REST resource.  

        :param object_type: The object_type of this ResourceGroupMemberRef.
        :type: str
        """

        self._object_type = object_type

    @property
    def moid(self):
        """
        Gets the moid of this ResourceGroupMemberRef.
        The Moid of the referenced REST resource.  

        :return: The moid of this ResourceGroupMemberRef.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ResourceGroupMemberRef.
        The Moid of the referenced REST resource.  

        :param moid: The moid of this ResourceGroupMemberRef.
        :type: str
        """

        self._moid = moid

    @property
    def selector(self):
        """
        Gets the selector of this ResourceGroupMemberRef.
        An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of 'moid' by clients. If 'moid' is set this field is ignored. If 'selector' is set and 'moid' is empty/absent from the request, Intersight will determine the Moid of the resource matching the filter expression and populate it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq '3AA8B7T11'.    

        :return: The selector of this ResourceGroupMemberRef.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this ResourceGroupMemberRef.
        An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of 'moid' by clients. If 'moid' is set this field is ignored. If 'selector' is set and 'moid' is empty/absent from the request, Intersight will determine the Moid of the resource matching the filter expression and populate it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq '3AA8B7T11'.    

        :param selector: The selector of this ResourceGroupMemberRef.
        :type: str
        """

        self._selector = selector

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
        if not isinstance(other, ResourceGroupMemberRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
