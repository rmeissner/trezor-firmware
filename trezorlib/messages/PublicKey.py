# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .HDNodeType import HDNodeType


class PublicKey(p.MessageType):
    FIELDS = {
        1: ('node', HDNodeType, 0),  # required
        2: ('xpub', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 12