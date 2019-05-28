# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class EthereumTypedDataRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 80

    def __init__(
        self,
        member_path: List[int] = None,
        signature: bytes = None,
        address: str = None,
    ) -> None:
        self.member_path = member_path if member_path is not None else []
        self.signature = signature
        self.address = address

    @classmethod
    def get_fields(cls):
        return {
            1: ('member_path', p.UVarintType, p.FLAG_REPEATED),
            2: ('signature', p.BytesType, 0),
            3: ('address', p.UnicodeType, 0),
        }