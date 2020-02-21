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


class NiaapiFieldNotice(object):
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
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoOptionalTag]',
        'version_context': 'MoOptionalVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'bugid': 'str',
        'field_notice_desc': 'str',
        'field_notice_id': 'str',
        'field_notice_url': 'str',
        'headline': 'str',
        'hwpid': 'str',
        'revision_info': 'list[NiaapiOptionalRevisionInfo]',
        'sw_release': 'str',
        'workaround_url': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'bugid': 'Bugid',
        'field_notice_desc': 'FieldNoticeDesc',
        'field_notice_id': 'FieldNoticeId',
        'field_notice_url': 'FieldNoticeUrl',
        'headline': 'Headline',
        'hwpid': 'Hwpid',
        'revision_info': 'RevisionInfo',
        'sw_release': 'SwRelease',
        'workaround_url': 'WorkaroundUrl'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, bugid=None, field_notice_desc=None, field_notice_id=None, field_notice_url=None, headline=None, hwpid=None, revision_info=None, sw_release=None, workaround_url=None):
        """
        NiaapiFieldNotice - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._bugid = None
        self._field_notice_desc = None
        self._field_notice_id = None
        self._field_notice_url = None
        self._headline = None
        self._hwpid = None
        self._revision_info = None
        self._sw_release = None
        self._workaround_url = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if bugid is not None:
          self.bugid = bugid
        if field_notice_desc is not None:
          self.field_notice_desc = field_notice_desc
        if field_notice_id is not None:
          self.field_notice_id = field_notice_id
        if field_notice_url is not None:
          self.field_notice_url = field_notice_url
        if headline is not None:
          self.headline = headline
        if hwpid is not None:
          self.hwpid = hwpid
        if revision_info is not None:
          self.revision_info = revision_info
        if sw_release is not None:
          self.sw_release = sw_release
        if workaround_url is not None:
          self.workaround_url = workaround_url

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NiaapiFieldNotice.
        The Account ID for this managed object.  

        :return: The account_moid of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NiaapiFieldNotice.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NiaapiFieldNotice.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this NiaapiFieldNotice.
        The time when this managed object was created.  

        :return: The create_time of this NiaapiFieldNotice.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NiaapiFieldNotice.
        The time when this managed object was created.  

        :param create_time: The create_time of this NiaapiFieldNotice.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NiaapiFieldNotice.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NiaapiFieldNotice.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NiaapiFieldNotice.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NiaapiFieldNotice.
        The time when this managed object was last modified.  

        :return: The mod_time of this NiaapiFieldNotice.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NiaapiFieldNotice.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NiaapiFieldNotice.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NiaapiFieldNotice.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NiaapiFieldNotice.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this NiaapiFieldNotice.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NiaapiFieldNotice.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NiaapiFieldNotice.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this NiaapiFieldNotice.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NiaapiFieldNotice.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NiaapiFieldNotice.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NiaapiFieldNotice.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NiaapiFieldNotice.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NiaapiFieldNotice.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NiaapiFieldNotice.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NiaapiFieldNotice.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NiaapiFieldNotice.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this NiaapiFieldNotice.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NiaapiFieldNotice.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this NiaapiFieldNotice.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NiaapiFieldNotice.
        The versioning info for this managed object.   

        :return: The version_context of this NiaapiFieldNotice.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NiaapiFieldNotice.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NiaapiFieldNotice.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NiaapiFieldNotice.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NiaapiFieldNotice.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NiaapiFieldNotice.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NiaapiFieldNotice.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this NiaapiFieldNotice.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NiaapiFieldNotice.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NiaapiFieldNotice.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NiaapiFieldNotice.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this NiaapiFieldNotice.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this NiaapiFieldNotice.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this NiaapiFieldNotice.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this NiaapiFieldNotice.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def bugid(self):
        """
        Gets the bugid of this NiaapiFieldNotice.
        Bug Id associated with this notice.  

        :return: The bugid of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._bugid

    @bugid.setter
    def bugid(self, bugid):
        """
        Sets the bugid of this NiaapiFieldNotice.
        Bug Id associated with this notice.  

        :param bugid: The bugid of this NiaapiFieldNotice.
        :type: str
        """

        self._bugid = bugid

    @property
    def field_notice_desc(self):
        """
        Gets the field_notice_desc of this NiaapiFieldNotice.
        Field notice Description.  

        :return: The field_notice_desc of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._field_notice_desc

    @field_notice_desc.setter
    def field_notice_desc(self, field_notice_desc):
        """
        Sets the field_notice_desc of this NiaapiFieldNotice.
        Field notice Description.  

        :param field_notice_desc: The field_notice_desc of this NiaapiFieldNotice.
        :type: str
        """

        self._field_notice_desc = field_notice_desc

    @property
    def field_notice_id(self):
        """
        Gets the field_notice_id of this NiaapiFieldNotice.
        Fieldnotice Id of this notice.  

        :return: The field_notice_id of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._field_notice_id

    @field_notice_id.setter
    def field_notice_id(self, field_notice_id):
        """
        Sets the field_notice_id of this NiaapiFieldNotice.
        Fieldnotice Id of this notice.  

        :param field_notice_id: The field_notice_id of this NiaapiFieldNotice.
        :type: str
        """

        self._field_notice_id = field_notice_id

    @property
    def field_notice_url(self):
        """
        Gets the field_notice_url of this NiaapiFieldNotice.
        Field notice URL link to the notice webpage.  

        :return: The field_notice_url of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._field_notice_url

    @field_notice_url.setter
    def field_notice_url(self, field_notice_url):
        """
        Sets the field_notice_url of this NiaapiFieldNotice.
        Field notice URL link to the notice webpage.  

        :param field_notice_url: The field_notice_url of this NiaapiFieldNotice.
        :type: str
        """

        self._field_notice_url = field_notice_url

    @property
    def headline(self):
        """
        Gets the headline of this NiaapiFieldNotice.
        The headline of this field notice.  

        :return: The headline of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this NiaapiFieldNotice.
        The headline of this field notice.  

        :param headline: The headline of this NiaapiFieldNotice.
        :type: str
        """

        self._headline = headline

    @property
    def hwpid(self):
        """
        Gets the hwpid of this NiaapiFieldNotice.
        Hardware PID for affected models.  

        :return: The hwpid of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._hwpid

    @hwpid.setter
    def hwpid(self, hwpid):
        """
        Sets the hwpid of this NiaapiFieldNotice.
        Hardware PID for affected models.  

        :param hwpid: The hwpid of this NiaapiFieldNotice.
        :type: str
        """

        self._hwpid = hwpid

    @property
    def revision_info(self):
        """
        Gets the revision_info of this NiaapiFieldNotice.
        Revision detail infomation .  

        :return: The revision_info of this NiaapiFieldNotice.
        :rtype: list[NiaapiOptionalRevisionInfo]
        """
        return self._revision_info

    @revision_info.setter
    def revision_info(self, revision_info):
        """
        Sets the revision_info of this NiaapiFieldNotice.
        Revision detail infomation .  

        :param revision_info: The revision_info of this NiaapiFieldNotice.
        :type: list[NiaapiOptionalRevisionInfo]
        """

        self._revision_info = revision_info

    @property
    def sw_release(self):
        """
        Gets the sw_release of this NiaapiFieldNotice.
        Software Release number for affected versions.  

        :return: The sw_release of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._sw_release

    @sw_release.setter
    def sw_release(self, sw_release):
        """
        Sets the sw_release of this NiaapiFieldNotice.
        Software Release number for affected versions.  

        :param sw_release: The sw_release of this NiaapiFieldNotice.
        :type: str
        """

        self._sw_release = sw_release

    @property
    def workaround_url(self):
        """
        Gets the workaround_url of this NiaapiFieldNotice.
        URL of workaround of this notice.   

        :return: The workaround_url of this NiaapiFieldNotice.
        :rtype: str
        """
        return self._workaround_url

    @workaround_url.setter
    def workaround_url(self, workaround_url):
        """
        Sets the workaround_url of this NiaapiFieldNotice.
        URL of workaround of this notice.   

        :param workaround_url: The workaround_url of this NiaapiFieldNotice.
        :type: str
        """

        self._workaround_url = workaround_url

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
        if not isinstance(other, NiaapiFieldNotice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
