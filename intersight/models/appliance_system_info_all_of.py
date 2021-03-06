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


class ApplianceSystemInfoAllOf(object):
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
        'cloud_conn_status': 'str',
        'deployment_size': 'str',
        'hostname': 'str',
        'init_done': 'bool',
        'operational_status': 'str',
        'serial_id': 'str',
        'time_zone': 'str',
        'version': 'str'
    }

    attribute_map = {
        'cloud_conn_status': 'CloudConnStatus',
        'deployment_size': 'DeploymentSize',
        'hostname': 'Hostname',
        'init_done': 'InitDone',
        'operational_status': 'OperationalStatus',
        'serial_id': 'SerialId',
        'time_zone': 'TimeZone',
        'version': 'Version'
    }

    def __init__(self,
                 cloud_conn_status='',
                 deployment_size=None,
                 hostname=None,
                 init_done=None,
                 operational_status='Unknown',
                 serial_id=None,
                 time_zone='Pacific/Niue',
                 version=None,
                 local_vars_configuration=None):  # noqa: E501
        """ApplianceSystemInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_conn_status = None
        self._deployment_size = None
        self._hostname = None
        self._init_done = None
        self._operational_status = None
        self._serial_id = None
        self._time_zone = None
        self._version = None
        self.discriminator = None

        if cloud_conn_status is not None:
            self.cloud_conn_status = cloud_conn_status
        if deployment_size is not None:
            self.deployment_size = deployment_size
        if hostname is not None:
            self.hostname = hostname
        if init_done is not None:
            self.init_done = init_done
        if operational_status is not None:
            self.operational_status = operational_status
        if serial_id is not None:
            self.serial_id = serial_id
        if time_zone is not None:
            self.time_zone = time_zone
        if version is not None:
            self.version = version

    @property
    def cloud_conn_status(self):
        """Gets the cloud_conn_status of this ApplianceSystemInfoAllOf.  # noqa: E501

        Connection state of the Intersight Appliance to the Intersight.     # noqa: E501

        :return: The cloud_conn_status of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cloud_conn_status

    @cloud_conn_status.setter
    def cloud_conn_status(self, cloud_conn_status):
        """Sets the cloud_conn_status of this ApplianceSystemInfoAllOf.

        Connection state of the Intersight Appliance to the Intersight.     # noqa: E501

        :param cloud_conn_status: The cloud_conn_status of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "Connected", "NotConnected",
                          "Unclaimed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cloud_conn_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cloud_conn_status` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_conn_status, allowed_values))

        self._cloud_conn_status = cloud_conn_status

    @property
    def deployment_size(self):
        """Gets the deployment_size of this ApplianceSystemInfoAllOf.  # noqa: E501

        Current running deployment size for the Intersight Appliance cluster. Eg. small, medium, large etc.    # noqa: E501

        :return: The deployment_size of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._deployment_size

    @deployment_size.setter
    def deployment_size(self, deployment_size):
        """Sets the deployment_size of this ApplianceSystemInfoAllOf.

        Current running deployment size for the Intersight Appliance cluster. Eg. small, medium, large etc.    # noqa: E501

        :param deployment_size: The deployment_size of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """

        self._deployment_size = deployment_size

    @property
    def hostname(self):
        """Gets the hostname of this ApplianceSystemInfoAllOf.  # noqa: E501

        Publicly accessible FQDN or IP address of the Intersight Appliance.    # noqa: E501

        :return: The hostname of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ApplianceSystemInfoAllOf.

        Publicly accessible FQDN or IP address of the Intersight Appliance.    # noqa: E501

        :param hostname: The hostname of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def init_done(self):
        """Gets the init_done of this ApplianceSystemInfoAllOf.  # noqa: E501

        Indicates that the setup initialization process has been completed.    # noqa: E501

        :return: The init_done of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._init_done

    @init_done.setter
    def init_done(self, init_done):
        """Sets the init_done of this ApplianceSystemInfoAllOf.

        Indicates that the setup initialization process has been completed.    # noqa: E501

        :param init_done: The init_done of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: bool
        """

        self._init_done = init_done

    @property
    def operational_status(self):
        """Gets the operational_status of this ApplianceSystemInfoAllOf.  # noqa: E501

        Operational status of the Intersight Appliance cluster.    # noqa: E501

        :return: The operational_status of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this ApplianceSystemInfoAllOf.

        Operational status of the Intersight Appliance cluster.    # noqa: E501

        :param operational_status: The operational_status of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Unknown", "Operational", "Impaired", "AttentionNeeded"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operational_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operational_status` ({0}), must be one of {1}"  # noqa: E501
                .format(operational_status, allowed_values))

        self._operational_status = operational_status

    @property
    def serial_id(self):
        """Gets the serial_id of this ApplianceSystemInfoAllOf.  # noqa: E501

        SerialId of the Intersight Appliance. SerialId is generated when the Intersight Appliance is setup. It is a unique UUID string, and serialId will not change for the life time of the Intersight Appliance.    # noqa: E501

        :return: The serial_id of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._serial_id

    @serial_id.setter
    def serial_id(self, serial_id):
        """Sets the serial_id of this ApplianceSystemInfoAllOf.

        SerialId of the Intersight Appliance. SerialId is generated when the Intersight Appliance is setup. It is a unique UUID string, and serialId will not change for the life time of the Intersight Appliance.    # noqa: E501

        :param serial_id: The serial_id of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """

        self._serial_id = serial_id

    @property
    def time_zone(self):
        """Gets the time_zone of this ApplianceSystemInfoAllOf.  # noqa: E501

        Timezone of the Intersight Appliance.    # noqa: E501

        :return: The time_zone of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ApplianceSystemInfoAllOf.

        Timezone of the Intersight Appliance.    # noqa: E501

        :param time_zone: The time_zone of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Pacific/Niue", "Pacific/Pago_Pago", "Pacific/Honolulu",
            "Pacific/Rarotonga", "Pacific/Tahiti", "Pacific/Marquesas",
            "America/Anchorage", "Pacific/Gambier", "America/Los_Angeles",
            "America/Tijuana", "America/Vancouver", "America/Whitehorse",
            "Pacific/Pitcairn", "America/Dawson_Creek", "America/Denver",
            "America/Edmonton", "America/Hermosillo", "America/Mazatlan",
            "America/Phoenix", "America/Yellowknife", "America/Belize",
            "America/Chicago", "America/Costa_Rica", "America/El_Salvador",
            "America/Guatemala", "America/Managua", "America/Mexico_City",
            "America/Regina", "America/Tegucigalpa", "America/Winnipeg",
            "Pacific/Galapagos", "America/Bogota", "America/Cancun",
            "America/Cayman", "America/Guayaquil", "America/Havana",
            "America/Iqaluit", "America/Jamaica", "America/Lima",
            "America/Nassau", "America/New_York", "America/Panama",
            "America/Port-au-Prince", "America/Rio_Branco", "America/Toronto",
            "Pacific/Easter", "America/Caracas", "America/Asuncion",
            "America/Barbados", "America/Boa_Vista", "America/Campo_Grande",
            "America/Cuiaba", "America/Curacao", "America/Grand_Turk",
            "America/Guyana", "America/Halifax", "America/La_Paz",
            "America/Manaus", "America/Martinique", "America/Port_of_Spain",
            "America/Porto_Velho", "America/Puerto_Rico",
            "America/Santo_Domingo", "America/Thule", "Atlantic/Bermuda",
            "America/St_Johns", "America/Araguaina",
            "America/Argentina/Buenos_Aires", "America/Bahia", "America/Belem",
            "America/Cayenne", "America/Fortaleza", "America/Godthab",
            "America/Maceio", "America/Miquelon", "America/Montevideo",
            "America/Paramaribo", "America/Recife", "America/Santiago",
            "America/Sao_Paulo", "Antarctica/Palmer", "Antarctica/Rothera",
            "Atlantic/Stanley", "America/Noronha", "Atlantic/South_Georgia",
            "America/Scoresbysund", "Atlantic/Azores", "Atlantic/Cape_Verde",
            "Africa/Abidjan", "Africa/Accra", "Africa/Bissau",
            "Africa/Casablanca", "Africa/El_Aaiun", "Africa/Monrovia",
            "America/Danmarkshavn", "Atlantic/Canary", "Atlantic/Faroe",
            "Atlantic/Reykjavik", "Etc/GMT", "Europe/Dublin", "Europe/Lisbon",
            "Europe/London", "Africa/Algiers", "Africa/Ceuta", "Africa/Lagos",
            "Africa/Ndjamena", "Africa/Tunis", "Africa/Windhoek",
            "Europe/Amsterdam", "Europe/Andorra", "Europe/Belgrade",
            "Europe/Berlin", "Europe/Brussels", "Europe/Budapest",
            "Europe/Copenhagen", "Europe/Gibraltar", "Europe/Luxembourg",
            "Europe/Madrid", "Europe/Malta", "Europe/Monaco", "Europe/Oslo",
            "Europe/Paris", "Europe/Prague", "Europe/Rome", "Europe/Stockholm",
            "Europe/Tirane", "Europe/Vienna", "Europe/Warsaw", "Europe/Zurich",
            "Africa/Cairo", "Africa/Johannesburg", "Africa/Maputo",
            "Africa/Tripoli", "Asia/Amman", "Asia/Beirut", "Asia/Damascus",
            "Asia/Gaza", "Asia/Jerusalem", "Asia/Nicosia", "Europe/Athens",
            "Europe/Bucharest", "Europe/Chisinau", "Europe/Helsinki",
            "Europe/Istanbul", "Europe/Kaliningrad", "Europe/Kiev",
            "Europe/Riga", "Europe/Sofia", "Europe/Tallinn", "Europe/Vilnius",
            "Africa/Khartoum", "Africa/Nairobi", "Antarctica/Syowa",
            "Asia/Baghdad", "Asia/Qatar", "Asia/Riyadh", "Europe/Minsk",
            "Europe/Moscow", "Asia/Tehran", "Asia/Baku", "Asia/Dubai",
            "Asia/Tbilisi", "Asia/Yerevan", "Europe/Samara", "Indian/Mahe",
            "Indian/Mauritius", "Indian/Reunion", "Asia/Kabul",
            "Antarctica/Mawson", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat",
            "Asia/Dushanbe", "Asia/Karachi", "Asia/Tashkent",
            "Asia/Yekaterinburg", "Indian/Kerguelen", "Indian/Maldives",
            "Asia/Calcutta", "Asia/Kolkata", "Asia/Colombo", "Asia/Katmandu",
            "Antarctica/Vostok", "Asia/Almaty", "Asia/Bishkek", "Asia/Dhaka",
            "Asia/Omsk", "Asia/Thimphu", "Indian/Chagos", "Asia/Rangoon",
            "Indian/Cocos", "Antarctica/Davis", "Asia/Bangkok", "Asia/Hovd",
            "Asia/Jakarta", "Asia/Krasnoyarsk", "Asia/Saigon",
            "Indian/Christmas", "Antarctica/Casey", "Asia/Brunei",
            "Asia/Choibalsan", "Asia/Hong_Kong", "Asia/Irkutsk",
            "Asia/Kuala_Lumpur", "Asia/Macau", "Asia/Makassar", "Asia/Manila",
            "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei",
            "Asia/Ulaanbaatar", "Australia/Perth", "Asia/Pyongyang",
            "Asia/Dili", "Asia/Jayapura", "Asia/Seoul", "Asia/Tokyo",
            "Asia/Yakutsk", "Pacific/Palau", "Australia/Adelaide",
            "Australia/Darwin", "Antarctica/DumontDUrville", "Asia/Magadan",
            "Asia/Vladivostok", "Australia/Brisbane", "Australia/Hobart",
            "Australia/Sydney", "Pacific/Chuuk", "Pacific/Guam",
            "Pacific/Port_Moresby", "Pacific/Efate", "Pacific/Guadalcanal",
            "Pacific/Kosrae", "Pacific/Norfolk", "Pacific/Noumea",
            "Pacific/Pohnpei", "Asia/Kamchatka", "Pacific/Auckland",
            "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Kwajalein",
            "Pacific/Majuro", "Pacific/Nauru", "Pacific/Tarawa",
            "Pacific/Wake", "Pacific/Wallis", "Pacific/Apia",
            "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Tongatapu",
            "Pacific/Kiritimati"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and time_zone not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(time_zone, allowed_values))

        self._time_zone = time_zone

    @property
    def version(self):
        """Gets the version of this ApplianceSystemInfoAllOf.  # noqa: E501

        Current software version of the Intersight Appliance.     # noqa: E501

        :return: The version of this ApplianceSystemInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApplianceSystemInfoAllOf.

        Current software version of the Intersight Appliance.     # noqa: E501

        :param version: The version of this ApplianceSystemInfoAllOf.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, ApplianceSystemInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceSystemInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
