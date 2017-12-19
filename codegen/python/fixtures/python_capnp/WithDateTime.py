"""
Auto-generated class for WithDateTime
"""
import capnp
import os
from datetime import datetime
from six import string_types

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class WithDateTime(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type birth: datetime
        :type name: str
        :rtype: WithDateTime
        """

        return WithDateTime(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'WithDateTime'
        data = json or kwargs

        # set attributes
        data_types = [datetime]
        self.birth = client_support.set_property('birth', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema WithDateTime.capnp
        :rtype bytes
        """
        template = capnp.load('%s/WithDateTime.capnp' % dir)
        return template.WithDateTime.new_message(**self.as_dict()).to_bytes()


class WithDateTimeCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of WithDateTime.capnp into class WithDateTime
        :type binary: bytes. If none creates an empty capnp object.
        rtype: WithDateTime
        """
        template = capnp.load('%s/WithDateTime.capnp' % dir)
        struct = template.WithDateTime.from_bytes(binary) if bin else template.WithDateTime.new_message()
        return WithDateTime(**struct.to_dict(verbose=True))