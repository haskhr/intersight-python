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


class NiaapiNewReleaseDetailAllOf(object):
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
        'description': 'str',
        'link': 'str',
        'release_note_link': 'str',
        'release_note_link_title': 'str',
        'software_download_link': 'str',
        'software_download_link_title': 'str',
        'title': 'str',
        'version': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'link': 'Link',
        'release_note_link': 'ReleaseNoteLink',
        'release_note_link_title': 'ReleaseNoteLinkTitle',
        'software_download_link': 'SoftwareDownloadLink',
        'software_download_link_title': 'SoftwareDownloadLinkTitle',
        'title': 'Title',
        'version': 'Version'
    }

    def __init__(self,
                 description=None,
                 link=None,
                 release_note_link=None,
                 release_note_link_title=None,
                 software_download_link=None,
                 software_download_link_title=None,
                 title=None,
                 version=None,
                 local_vars_configuration=None):  # noqa: E501
        """NiaapiNewReleaseDetailAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._link = None
        self._release_note_link = None
        self._release_note_link_title = None
        self._software_download_link = None
        self._software_download_link_title = None
        self._title = None
        self._version = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if link is not None:
            self.link = link
        if release_note_link is not None:
            self.release_note_link = release_note_link
        if release_note_link_title is not None:
            self.release_note_link_title = release_note_link_title
        if software_download_link is not None:
            self.software_download_link = software_download_link
        if software_download_link_title is not None:
            self.software_download_link_title = software_download_link_title
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version

    @property
    def description(self):
        """Gets the description of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        Description of this new verison release post.    # noqa: E501

        :return: The description of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NiaapiNewReleaseDetailAllOf.

        Description of this new verison release post.    # noqa: E501

        :param description: The description of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def link(self):
        """Gets the link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        Link of downloading the release file.    # noqa: E501

        :return: The link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this NiaapiNewReleaseDetailAllOf.

        Link of downloading the release file.    # noqa: E501

        :param link: The link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def release_note_link(self):
        """Gets the release_note_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        The link used to provide a gateway for customer to review the release note.    # noqa: E501

        :return: The release_note_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._release_note_link

    @release_note_link.setter
    def release_note_link(self, release_note_link):
        """Sets the release_note_link of this NiaapiNewReleaseDetailAllOf.

        The link used to provide a gateway for customer to review the release note.    # noqa: E501

        :param release_note_link: The release_note_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._release_note_link = release_note_link

    @property
    def release_note_link_title(self):
        """Gets the release_note_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        The link title used to provide a gateway for customer to review the release note.    # noqa: E501

        :return: The release_note_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._release_note_link_title

    @release_note_link_title.setter
    def release_note_link_title(self, release_note_link_title):
        """Sets the release_note_link_title of this NiaapiNewReleaseDetailAllOf.

        The link title used to provide a gateway for customer to review the release note.    # noqa: E501

        :param release_note_link_title: The release_note_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._release_note_link_title = release_note_link_title

    @property
    def software_download_link(self):
        """Gets the software_download_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        The link used to provide a gateway for customer to download the release.    # noqa: E501

        :return: The software_download_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._software_download_link

    @software_download_link.setter
    def software_download_link(self, software_download_link):
        """Sets the software_download_link of this NiaapiNewReleaseDetailAllOf.

        The link used to provide a gateway for customer to download the release.    # noqa: E501

        :param software_download_link: The software_download_link of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._software_download_link = software_download_link

    @property
    def software_download_link_title(self):
        """Gets the software_download_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        The link title used to provide a gateway for customer to download the release.    # noqa: E501

        :return: The software_download_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._software_download_link_title

    @software_download_link_title.setter
    def software_download_link_title(self, software_download_link_title):
        """Sets the software_download_link_title of this NiaapiNewReleaseDetailAllOf.

        The link title used to provide a gateway for customer to download the release.    # noqa: E501

        :param software_download_link_title: The software_download_link_title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._software_download_link_title = software_download_link_title

    @property
    def title(self):
        """Gets the title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        Title of the new verison release post.    # noqa: E501

        :return: The title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NiaapiNewReleaseDetailAllOf.

        Title of the new verison release post.    # noqa: E501

        :param title: The title of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this NiaapiNewReleaseDetailAllOf.  # noqa: E501

        Version number Associate with this Post.     # noqa: E501

        :return: The version of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NiaapiNewReleaseDetailAllOf.

        Version number Associate with this Post.     # noqa: E501

        :param version: The version of this NiaapiNewReleaseDetailAllOf.  # noqa: E501
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
        if not isinstance(other, NiaapiNewReleaseDetailAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NiaapiNewReleaseDetailAllOf):
            return True

        return self.to_dict() != other.to_dict()