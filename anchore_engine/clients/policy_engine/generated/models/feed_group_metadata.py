# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeedGroupMetadata(object):
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
        'name': 'str',
        'created_at': 'datetime',
        'last_sync': 'datetime',
        'record_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'last_sync': 'last_sync',
        'record_count': 'record_count'
    }

    def __init__(self, name=None, created_at=None, last_sync=None, record_count=None):  # noqa: E501
        """FeedGroupMetadata - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._created_at = None
        self._last_sync = None
        self._record_count = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if last_sync is not None:
            self.last_sync = last_sync
        if record_count is not None:
            self.record_count = record_count

    @property
    def name(self):
        """Gets the name of this FeedGroupMetadata.  # noqa: E501


        :return: The name of this FeedGroupMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeedGroupMetadata.


        :param name: The name of this FeedGroupMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this FeedGroupMetadata.  # noqa: E501


        :return: The created_at of this FeedGroupMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FeedGroupMetadata.


        :param created_at: The created_at of this FeedGroupMetadata.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def last_sync(self):
        """Gets the last_sync of this FeedGroupMetadata.  # noqa: E501


        :return: The last_sync of this FeedGroupMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this FeedGroupMetadata.


        :param last_sync: The last_sync of this FeedGroupMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_sync = last_sync

    @property
    def record_count(self):
        """Gets the record_count of this FeedGroupMetadata.  # noqa: E501


        :return: The record_count of this FeedGroupMetadata.  # noqa: E501
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this FeedGroupMetadata.


        :param record_count: The record_count of this FeedGroupMetadata.  # noqa: E501
        :type: int
        """

        self._record_count = record_count

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeedGroupMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
