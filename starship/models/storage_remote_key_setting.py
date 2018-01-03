# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageRemoteKeySetting(object):
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
        'password': 'str',
        'port': 'int',
        'primary_server': 'str',
        'secondary_server': 'str',
        'server_certificate': 'str',
        'username': 'str'
    }

    attribute_map = {
        'password': 'Password',
        'port': 'Port',
        'primary_server': 'PrimaryServer',
        'secondary_server': 'SecondaryServer',
        'server_certificate': 'ServerCertificate',
        'username': 'Username'
    }

    def __init__(self, password=None, port=None, primary_server=None, secondary_server=None, server_certificate=None, username=None):
        """
        StorageRemoteKeySetting - a model defined in Swagger
        """

        self._password = None
        self._port = None
        self._primary_server = None
        self._secondary_server = None
        self._server_certificate = None
        self._username = None

        if password is not None:
          self.password = password
        if port is not None:
          self.port = port
        if primary_server is not None:
          self.primary_server = primary_server
        if secondary_server is not None:
          self.secondary_server = secondary_server
        if server_certificate is not None:
          self.server_certificate = server_certificate
        if username is not None:
          self.username = username

    @property
    def password(self):
        """
        Gets the password of this StorageRemoteKeySetting.
        This property is used to specify password for the KMIP server login  

        :return: The password of this StorageRemoteKeySetting.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this StorageRemoteKeySetting.
        This property is used to specify password for the KMIP server login  

        :param password: The password of this StorageRemoteKeySetting.
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """
        Gets the port of this StorageRemoteKeySetting.
        This property is used to port to which the KMIP client should connect  

        :return: The port of this StorageRemoteKeySetting.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this StorageRemoteKeySetting.
        This property is used to port to which the KMIP client should connect  

        :param port: The port of this StorageRemoteKeySetting.
        :type: int
        """

        self._port = port

    @property
    def primary_server(self):
        """
        Gets the primary_server of this StorageRemoteKeySetting.
        This property is used to store the address of the KMIP server. It could be an IPv4 address or an IPv6 address or hostname. Hostnames are valid only when Inband is configured for the CIMC address.  

        :return: The primary_server of this StorageRemoteKeySetting.
        :rtype: str
        """
        return self._primary_server

    @primary_server.setter
    def primary_server(self, primary_server):
        """
        Sets the primary_server of this StorageRemoteKeySetting.
        This property is used to store the address of the KMIP server. It could be an IPv4 address or an IPv6 address or hostname. Hostnames are valid only when Inband is configured for the CIMC address.  

        :param primary_server: The primary_server of this StorageRemoteKeySetting.
        :type: str
        """

        self._primary_server = primary_server

    @property
    def secondary_server(self):
        """
        Gets the secondary_server of this StorageRemoteKeySetting.
        This property is used to store the address of the KMIP server. It could be an IPv4 address or an IPv6 address or hostname. Hostnames are valid only when Inband is configured for the CIMC address.  

        :return: The secondary_server of this StorageRemoteKeySetting.
        :rtype: str
        """
        return self._secondary_server

    @secondary_server.setter
    def secondary_server(self, secondary_server):
        """
        Sets the secondary_server of this StorageRemoteKeySetting.
        This property is used to store the address of the KMIP server. It could be an IPv4 address or an IPv6 address or hostname. Hostnames are valid only when Inband is configured for the CIMC address.  

        :param secondary_server: The secondary_server of this StorageRemoteKeySetting.
        :type: str
        """

        self._secondary_server = secondary_server

    @property
    def server_certificate(self):
        """
        Gets the server_certificate of this StorageRemoteKeySetting.
        This property is used to store the certificate/ public key of the KMIP server This is required for initiating secure communication with the server  

        :return: The server_certificate of this StorageRemoteKeySetting.
        :rtype: str
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """
        Sets the server_certificate of this StorageRemoteKeySetting.
        This property is used to store the certificate/ public key of the KMIP server This is required for initiating secure communication with the server  

        :param server_certificate: The server_certificate of this StorageRemoteKeySetting.
        :type: str
        """

        self._server_certificate = server_certificate

    @property
    def username(self):
        """
        Gets the username of this StorageRemoteKeySetting.
        This property is used to specify user name for the KMIP server login   

        :return: The username of this StorageRemoteKeySetting.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this StorageRemoteKeySetting.
        This property is used to specify user name for the KMIP server login   

        :param username: The username of this StorageRemoteKeySetting.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, StorageRemoteKeySetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other