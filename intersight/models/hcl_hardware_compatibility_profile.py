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


class HclHardwareCompatibilityProfile(object):
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
        'driver_iso_url': 'str',
        'error_code': 'str',
        'id': 'str',
        'os_vendor': 'str',
        'os_version': 'str',
        'processor_model': 'str',
        'products': 'list[HclProduct]',
        'server_model': 'str',
        'server_revision': 'str',
        'ucs_version': 'str',
        'version_type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'driver_iso_url': 'DriverIsoUrl',
        'error_code': 'ErrorCode',
        'id': 'Id',
        'os_vendor': 'OsVendor',
        'os_version': 'OsVersion',
        'processor_model': 'ProcessorModel',
        'products': 'Products',
        'server_model': 'ServerModel',
        'server_revision': 'ServerRevision',
        'ucs_version': 'UcsVersion',
        'version_type': 'VersionType'
    }

    def __init__(self, object_type=None, driver_iso_url=None, error_code='Success', id=None, os_vendor=None, os_version=None, processor_model=None, products=None, server_model=None, server_revision=None, ucs_version=None, version_type='UCSM'):
        """
        HclHardwareCompatibilityProfile - a model defined in Swagger
        """

        self._object_type = None
        self._driver_iso_url = None
        self._error_code = None
        self._id = None
        self._os_vendor = None
        self._os_version = None
        self._processor_model = None
        self._products = None
        self._server_model = None
        self._server_revision = None
        self._ucs_version = None
        self._version_type = None

        if object_type is not None:
          self.object_type = object_type
        if driver_iso_url is not None:
          self.driver_iso_url = driver_iso_url
        if error_code is not None:
          self.error_code = error_code
        if id is not None:
          self.id = id
        if os_vendor is not None:
          self.os_vendor = os_vendor
        if os_version is not None:
          self.os_version = os_version
        if processor_model is not None:
          self.processor_model = processor_model
        if products is not None:
          self.products = products
        if server_model is not None:
          self.server_model = server_model
        if server_revision is not None:
          self.server_revision = server_revision
        if ucs_version is not None:
          self.ucs_version = ucs_version
        if version_type is not None:
          self.version_type = version_type

    @property
    def object_type(self):
        """
        Gets the object_type of this HclHardwareCompatibilityProfile.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HclHardwareCompatibilityProfile.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def driver_iso_url(self):
        """
        Gets the driver_iso_url of this HclHardwareCompatibilityProfile.
        Url for the ISO with the drivers supported for the server.

        :return: The driver_iso_url of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._driver_iso_url

    @driver_iso_url.setter
    def driver_iso_url(self, driver_iso_url):
        """
        Sets the driver_iso_url of this HclHardwareCompatibilityProfile.
        Url for the ISO with the drivers supported for the server.

        :param driver_iso_url: The driver_iso_url of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._driver_iso_url = driver_iso_url

    @property
    def error_code(self):
        """
        Gets the error_code of this HclHardwareCompatibilityProfile.
        Error code indicating the compatibility status.

        :return: The error_code of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this HclHardwareCompatibilityProfile.
        Error code indicating the compatibility status.

        :param error_code: The error_code of this HclHardwareCompatibilityProfile.
        :type: str
        """
        allowed_values = ["Success", "Unknown", "UnknownServer", "InvalidUcsVersion", "ProcessorNotSupported", "OSNotSupported", "OSUnknown", "UCSVersionNotSupported", "UcsVersionServerOSCombinationNotSupported", "ProductUnknown", "ProductNotSupported", "DriverNameNotSupported", "FirmwareVersionNotSupported", "DriverVersionNotSupported", "FirmwareVersionDriverVersionCombinationNotSupported", "FirmwareVersionAndDriverVersionNotSupported", "FirmwareVersionAndDriverNameNotSupported", "InternalError", "MarshallingError", "Exempted"]
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def id(self):
        """
        Gets the id of this HclHardwareCompatibilityProfile.
        Identifier of the hardware compatibility profile.

        :return: The id of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HclHardwareCompatibilityProfile.
        Identifier of the hardware compatibility profile.

        :param id: The id of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._id = id

    @property
    def os_vendor(self):
        """
        Gets the os_vendor of this HclHardwareCompatibilityProfile.
        Vendor of the Operating System running on the server.

        :return: The os_vendor of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._os_vendor

    @os_vendor.setter
    def os_vendor(self, os_vendor):
        """
        Sets the os_vendor of this HclHardwareCompatibilityProfile.
        Vendor of the Operating System running on the server.

        :param os_vendor: The os_vendor of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._os_vendor = os_vendor

    @property
    def os_version(self):
        """
        Gets the os_version of this HclHardwareCompatibilityProfile.
        Version of the Operating System running on the server.

        :return: The os_version of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this HclHardwareCompatibilityProfile.
        Version of the Operating System running on the server.

        :param os_version: The os_version of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._os_version = os_version

    @property
    def processor_model(self):
        """
        Gets the processor_model of this HclHardwareCompatibilityProfile.
        Model of the processor present in the server.

        :return: The processor_model of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._processor_model

    @processor_model.setter
    def processor_model(self, processor_model):
        """
        Sets the processor_model of this HclHardwareCompatibilityProfile.
        Model of the processor present in the server.

        :param processor_model: The processor_model of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._processor_model = processor_model

    @property
    def products(self):
        """
        Gets the products of this HclHardwareCompatibilityProfile.
        List of the products (adapters/storage controllers) for which compatibility status needs to be checked.

        :return: The products of this HclHardwareCompatibilityProfile.
        :rtype: list[HclProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this HclHardwareCompatibilityProfile.
        List of the products (adapters/storage controllers) for which compatibility status needs to be checked.

        :param products: The products of this HclHardwareCompatibilityProfile.
        :type: list[HclProduct]
        """

        self._products = products

    @property
    def server_model(self):
        """
        Gets the server_model of this HclHardwareCompatibilityProfile.
        Model of the server as returned by UCSM/CIMC XML API.

        :return: The server_model of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._server_model

    @server_model.setter
    def server_model(self, server_model):
        """
        Sets the server_model of this HclHardwareCompatibilityProfile.
        Model of the server as returned by UCSM/CIMC XML API.

        :param server_model: The server_model of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._server_model = server_model

    @property
    def server_revision(self):
        """
        Gets the server_revision of this HclHardwareCompatibilityProfile.
        Revision of the server model.

        :return: The server_revision of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._server_revision

    @server_revision.setter
    def server_revision(self, server_revision):
        """
        Sets the server_revision of this HclHardwareCompatibilityProfile.
        Revision of the server model.

        :param server_revision: The server_revision of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._server_revision = server_revision

    @property
    def ucs_version(self):
        """
        Gets the ucs_version of this HclHardwareCompatibilityProfile.
        Version of the UCS software.

        :return: The ucs_version of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._ucs_version

    @ucs_version.setter
    def ucs_version(self, ucs_version):
        """
        Sets the ucs_version of this HclHardwareCompatibilityProfile.
        Version of the UCS software.

        :param ucs_version: The ucs_version of this HclHardwareCompatibilityProfile.
        :type: str
        """

        self._ucs_version = ucs_version

    @property
    def version_type(self):
        """
        Gets the version_type of this HclHardwareCompatibilityProfile.
        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.

        :return: The version_type of this HclHardwareCompatibilityProfile.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """
        Sets the version_type of this HclHardwareCompatibilityProfile.
        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.

        :param version_type: The version_type of this HclHardwareCompatibilityProfile.
        :type: str
        """
        allowed_values = ["UCSM", "IMC"]
        if version_type not in allowed_values:
            raise ValueError(
                "Invalid value for `version_type` ({0}), must be one of {1}"
                .format(version_type, allowed_values)
            )

        self._version_type = version_type

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
        if not isinstance(other, HclHardwareCompatibilityProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
