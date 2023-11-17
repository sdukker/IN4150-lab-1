from ipv8.messaging.payload_dataclass import overwrite_dataclass
from dataclasses import dataclass

from src.da_types import *
from ipv8.types import Peer

# We are using a custom dataclass implementation.
dataclass = overwrite_dataclass(dataclass)


@dataclass(
    msg_id=1
)  # The value 1 identifies this message and must be unique per community.
class MyMessage:
    pass

class EchoAlgorithm(DistributedAlgorithm):

    def __init__(self, settings: CommunitySettings) -> None:
        super().__init__(settings)

        self.add_message_handler(MyMessage, self.on_message)

    def on_start(self):
        pass

    @message_wrapper(MyMessage)
    async def on_message(self, peer: Peer, payload: MyMessage) -> None:
        pass
