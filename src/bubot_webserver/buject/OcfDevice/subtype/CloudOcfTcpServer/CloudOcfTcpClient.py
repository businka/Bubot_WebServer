import asyncio
from .OcfTcpClientProtocol import OcfTcpClientProtocol


class CloudOcfTcpClient:

    def connect_to_cloud(self):
        loop = asyncio.get_running_loop()

        on_con_lost = loop.create_future()
        message = 'Hello World!'

        transport, protocol = await loop.create_connection(
            lambda: OcfTcpClientProtocol(message, on_con_lost),
            '127.0.0.1', 8888)

        # Wait until the protocol signals that the connection
        # is lost and close the transport.
        try:
            await on_con_lost
        finally:
            transport.close()