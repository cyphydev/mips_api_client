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

class RawDataPostEntry(object):
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
        'source': 'Source',
        'items': 'list[Item]'
    }

    attribute_map = {
        'source': 'source',
        'items': 'items'
    }

    def __init__(self, source=None, items=None):  # noqa: E501
        """RawDataPostEntry - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._items = None
        self.discriminator = None
        self.source = source
        self.items = items

    @property
    def source(self):
        """Gets the source of this RawDataPostEntry.  # noqa: E501


        :return: The source of this RawDataPostEntry.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RawDataPostEntry.


        :param source: The source of this RawDataPostEntry.  # noqa: E501
        :type: Source
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def items(self):
        """Gets the items of this RawDataPostEntry.  # noqa: E501


        :return: The items of this RawDataPostEntry.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RawDataPostEntry.


        :param items: The items of this RawDataPostEntry.  # noqa: E501
        :type: list[Item]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

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
        if issubclass(RawDataPostEntry, dict):
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
        if not isinstance(other, RawDataPostEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
