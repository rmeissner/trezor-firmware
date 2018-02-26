# Automatically generated by pb2py
import protobuf as p


class NEMTransactionCommon(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('network', p.UVarintType, 0),
        3: ('timestamp', p.UVarintType, 0),
        4: ('fee', p.UVarintType, 0),
        5: ('deadline', p.UVarintType, 0),
        6: ('signer', p.BytesType, 0),
    }

    def __init__(
        self,
        address_n: list = [],
        network: int = None,
        timestamp: int = None,
        fee: int = None,
        deadline: int = None,
        signer: bytes = None,
        **kwargs,
    ):
        self.address_n = address_n
        self.network = network
        self.timestamp = timestamp
        self.fee = fee
        self.deadline = deadline
        self.signer = signer
        p.MessageType.__init__(self, **kwargs)
