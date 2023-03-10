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

class BatchGetRequest(object):
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
        'ids': 'list[int]',
        'with_enrichment': 'bool',
        'enrichment_name': 'str',
        'enrichment_provider': 'str',
        'enrichment_tag': 'str',
        'enrichment_version': 'str',
        'with_cluster': 'bool',
        'cluster_name': 'str',
        'cluster_provider': 'str',
        'cluster_tag': 'str',
        'cluster_version': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'with_enrichment': 'with_enrichment',
        'enrichment_name': 'enrichment_name',
        'enrichment_provider': 'enrichment_provider',
        'enrichment_tag': 'enrichment_tag',
        'enrichment_version': 'enrichment_version',
        'with_cluster': 'with_cluster',
        'cluster_name': 'cluster_name',
        'cluster_provider': 'cluster_provider',
        'cluster_tag': 'cluster_tag',
        'cluster_version': 'cluster_version'
    }

    def __init__(self, ids=None, with_enrichment=None, enrichment_name=None, enrichment_provider=None, enrichment_tag=None, enrichment_version=None, with_cluster=None, cluster_name=None, cluster_provider=None, cluster_tag=None, cluster_version=None):  # noqa: E501
        """BatchGetRequest - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._with_enrichment = None
        self._enrichment_name = None
        self._enrichment_provider = None
        self._enrichment_tag = None
        self._enrichment_version = None
        self._with_cluster = None
        self._cluster_name = None
        self._cluster_provider = None
        self._cluster_tag = None
        self._cluster_version = None
        self.discriminator = None
        self.ids = ids
        if with_enrichment is not None:
            self.with_enrichment = with_enrichment
        if enrichment_name is not None:
            self.enrichment_name = enrichment_name
        if enrichment_provider is not None:
            self.enrichment_provider = enrichment_provider
        if enrichment_tag is not None:
            self.enrichment_tag = enrichment_tag
        if enrichment_version is not None:
            self.enrichment_version = enrichment_version
        if with_cluster is not None:
            self.with_cluster = with_cluster
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_provider is not None:
            self.cluster_provider = cluster_provider
        if cluster_tag is not None:
            self.cluster_tag = cluster_tag
        if cluster_version is not None:
            self.cluster_version = cluster_version

    @property
    def ids(self):
        """Gets the ids of this BatchGetRequest.  # noqa: E501


        :return: The ids of this BatchGetRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this BatchGetRequest.


        :param ids: The ids of this BatchGetRequest.  # noqa: E501
        :type: list[int]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def with_enrichment(self):
        """Gets the with_enrichment of this BatchGetRequest.  # noqa: E501


        :return: The with_enrichment of this BatchGetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._with_enrichment

    @with_enrichment.setter
    def with_enrichment(self, with_enrichment):
        """Sets the with_enrichment of this BatchGetRequest.


        :param with_enrichment: The with_enrichment of this BatchGetRequest.  # noqa: E501
        :type: bool
        """

        self._with_enrichment = with_enrichment

    @property
    def enrichment_name(self):
        """Gets the enrichment_name of this BatchGetRequest.  # noqa: E501


        :return: The enrichment_name of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_name

    @enrichment_name.setter
    def enrichment_name(self, enrichment_name):
        """Sets the enrichment_name of this BatchGetRequest.


        :param enrichment_name: The enrichment_name of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._enrichment_name = enrichment_name

    @property
    def enrichment_provider(self):
        """Gets the enrichment_provider of this BatchGetRequest.  # noqa: E501


        :return: The enrichment_provider of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_provider

    @enrichment_provider.setter
    def enrichment_provider(self, enrichment_provider):
        """Sets the enrichment_provider of this BatchGetRequest.


        :param enrichment_provider: The enrichment_provider of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._enrichment_provider = enrichment_provider

    @property
    def enrichment_tag(self):
        """Gets the enrichment_tag of this BatchGetRequest.  # noqa: E501


        :return: The enrichment_tag of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_tag

    @enrichment_tag.setter
    def enrichment_tag(self, enrichment_tag):
        """Sets the enrichment_tag of this BatchGetRequest.


        :param enrichment_tag: The enrichment_tag of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._enrichment_tag = enrichment_tag

    @property
    def enrichment_version(self):
        """Gets the enrichment_version of this BatchGetRequest.  # noqa: E501


        :return: The enrichment_version of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_version

    @enrichment_version.setter
    def enrichment_version(self, enrichment_version):
        """Sets the enrichment_version of this BatchGetRequest.


        :param enrichment_version: The enrichment_version of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._enrichment_version = enrichment_version

    @property
    def with_cluster(self):
        """Gets the with_cluster of this BatchGetRequest.  # noqa: E501


        :return: The with_cluster of this BatchGetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._with_cluster

    @with_cluster.setter
    def with_cluster(self, with_cluster):
        """Sets the with_cluster of this BatchGetRequest.


        :param with_cluster: The with_cluster of this BatchGetRequest.  # noqa: E501
        :type: bool
        """

        self._with_cluster = with_cluster

    @property
    def cluster_name(self):
        """Gets the cluster_name of this BatchGetRequest.  # noqa: E501


        :return: The cluster_name of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this BatchGetRequest.


        :param cluster_name: The cluster_name of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_provider(self):
        """Gets the cluster_provider of this BatchGetRequest.  # noqa: E501


        :return: The cluster_provider of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_provider

    @cluster_provider.setter
    def cluster_provider(self, cluster_provider):
        """Sets the cluster_provider of this BatchGetRequest.


        :param cluster_provider: The cluster_provider of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._cluster_provider = cluster_provider

    @property
    def cluster_tag(self):
        """Gets the cluster_tag of this BatchGetRequest.  # noqa: E501


        :return: The cluster_tag of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_tag

    @cluster_tag.setter
    def cluster_tag(self, cluster_tag):
        """Sets the cluster_tag of this BatchGetRequest.


        :param cluster_tag: The cluster_tag of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._cluster_tag = cluster_tag

    @property
    def cluster_version(self):
        """Gets the cluster_version of this BatchGetRequest.  # noqa: E501


        :return: The cluster_version of this BatchGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """Sets the cluster_version of this BatchGetRequest.


        :param cluster_version: The cluster_version of this BatchGetRequest.  # noqa: E501
        :type: str
        """

        self._cluster_version = cluster_version

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
        if issubclass(BatchGetRequest, dict):
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
        if not isinstance(other, BatchGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
