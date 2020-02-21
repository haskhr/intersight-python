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


class AssetSudiInfo(object):
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
        'pid': 'str',
        'serial_number': 'str',
        'signature': 'str',
        'status': 'str',
        'sudi_certificate': 'X509OptionalCertificate'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'pid': 'Pid',
        'serial_number': 'SerialNumber',
        'signature': 'Signature',
        'status': 'Status',
        'sudi_certificate': 'SudiCertificate'
    }

    def __init__(self, object_type=None, pid=None, serial_number=None, signature=None, status='DeviceStatusUnknown', sudi_certificate=None):
        """
        AssetSudiInfo - a model defined in Swagger
        """

        self._object_type = None
        self._pid = None
        self._serial_number = None
        self._signature = None
        self._status = None
        self._sudi_certificate = None

        if object_type is not None:
          self.object_type = object_type
        if pid is not None:
          self.pid = pid
        if serial_number is not None:
          self.serial_number = serial_number
        if signature is not None:
          self.signature = signature
        if status is not None:
          self.status = status
        if sudi_certificate is not None:
          self.sudi_certificate = sudi_certificate

    @property
    def object_type(self):
        """
        Gets the object_type of this AssetSudiInfo.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this AssetSudiInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AssetSudiInfo.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this AssetSudiInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def pid(self):
        """
        Gets the pid of this AssetSudiInfo.
        The device model (PID) extracted from the X.509 SUDI Leaf Certificate.  

        :return: The pid of this AssetSudiInfo.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this AssetSudiInfo.
        The device model (PID) extracted from the X.509 SUDI Leaf Certificate.  

        :param pid: The pid of this AssetSudiInfo.
        :type: str
        """

        self._pid = pid

    @property
    def serial_number(self):
        """
        Gets the serial_number of this AssetSudiInfo.
        The device SerialNumber extracted from the X.509 SUDI Leaf Certiicate.  

        :return: The serial_number of this AssetSudiInfo.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this AssetSudiInfo.
        The device SerialNumber extracted from the X.509 SUDI Leaf Certiicate.  

        :param serial_number: The serial_number of this AssetSudiInfo.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signature(self):
        """
        Gets the signature of this AssetSudiInfo.
        The signature is obtained by taking the base64 encoding of the Serial Number + PID + Status, taking the SHA256 hash and then signing with the SUDI X.509 Leaf Certifiate.  

        :return: The signature of this AssetSudiInfo.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this AssetSudiInfo.
        The signature is obtained by taking the base64 encoding of the Serial Number + PID + Status, taking the SHA256 hash and then signing with the SUDI X.509 Leaf Certifiate.  

        :param signature: The signature of this AssetSudiInfo.
        :type: str
        """

        self._signature = signature

    @property
    def status(self):
        """
        Gets the status of this AssetSudiInfo.
        The validation status of the device.  

        :return: The status of this AssetSudiInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AssetSudiInfo.
        The validation status of the device.  

        :param status: The status of this AssetSudiInfo.
        :type: str
        """
        allowed_values = ["DeviceStatusUnknown", "Verified", "CertificateValidationFailed", "UnsupportedFirmware", "UnsupportedHardware", "DeviceNotResponding"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sudi_certificate(self):
        """
        Gets the sudi_certificate of this AssetSudiInfo.
        The X.509 SUDI Leaf Certificate from the Trust Anchor Module. The certificate is serialized in PEM format (Base64 encoded DER certificate).   

        :return: The sudi_certificate of this AssetSudiInfo.
        :rtype: X509OptionalCertificate
        """
        return self._sudi_certificate

    @sudi_certificate.setter
    def sudi_certificate(self, sudi_certificate):
        """
        Sets the sudi_certificate of this AssetSudiInfo.
        The X.509 SUDI Leaf Certificate from the Trust Anchor Module. The certificate is serialized in PEM format (Base64 encoded DER certificate).   

        :param sudi_certificate: The sudi_certificate of this AssetSudiInfo.
        :type: X509OptionalCertificate
        """

        self._sudi_certificate = sudi_certificate

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
        if not isinstance(other, AssetSudiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
