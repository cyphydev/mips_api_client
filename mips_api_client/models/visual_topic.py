# coding: utf-8

"""
    Mips UIUC Datatypes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VisualTopic(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'int',
        'name': 'str',
        'provider': 'str',
        'tag': 'str',
        'version': 'str',
        'type': 'ClusterType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'tag': 'tag',
        'version': 'version',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, provider=None, tag=None, version=None, type=None):  # noqa: E501
        """VisualTopic - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._provider = None
        self._tag = None
        self._version = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.provider = provider
        self.tag = tag
        self.version = version
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this VisualTopic.  # noqa: E501


        :return: The id of this VisualTopic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VisualTopic.


        :param id: The id of this VisualTopic.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VisualTopic.  # noqa: E501

        The enrichment (e.g., Concern-Stance) name for the enrichment.  # noqa: E501

        :return: The name of this VisualTopic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VisualTopic.

        The enrichment (e.g., Concern-Stance) name for the enrichment.  # noqa: E501

        :param name: The name of this VisualTopic.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this VisualTopic.  # noqa: E501

        The team (e.g., UIUC-DMG) who provides the enrichment.  # noqa: E501

        :return: The provider of this VisualTopic.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VisualTopic.

        The team (e.g., UIUC-DMG) who provides the enrichment.  # noqa: E501

        :param provider: The provider of this VisualTopic.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def tag(self):
        """Gets the tag of this VisualTopic.  # noqa: E501

        The tag within the same (provider, name).  # noqa: E501

        :return: The tag of this VisualTopic.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this VisualTopic.

        The tag within the same (provider, name).  # noqa: E501

        :param tag: The tag of this VisualTopic.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def version(self):
        """Gets the version of this VisualTopic.  # noqa: E501

        The version within the same (provider, name).  # noqa: E501

        :return: The version of this VisualTopic.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VisualTopic.

        The version within the same (provider, name).  # noqa: E501

        :param version: The version of this VisualTopic.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def type(self):
        """Gets the type of this VisualTopic.  # noqa: E501


        :return: The type of this VisualTopic.  # noqa: E501
        :rtype: ClusterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VisualTopic.


        :param type: The type of this VisualTopic.  # noqa: E501
        :type: ClusterType
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(VisualTopic, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VisualTopic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
