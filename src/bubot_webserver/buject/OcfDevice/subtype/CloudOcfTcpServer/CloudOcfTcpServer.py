# from bubot_thermostat_sml1000 import __version__ as device_version
import asyncio
import logging

from bubot.buject.OcfDevice.subtype.Device.Device import Device
from .OcfTcpServerProtocol import OcfTcpServerProtocol

_logger = logging.getLogger(__name__)


class CloudOcfTcpServer:
    version = '0.0.1'
    file = __file__

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # async def on_pending(self):
    #     await self.start_ocf_tcp_server()

    async def start_ocf_tcp_server(self):
        loop = asyncio.get_running_loop()
        server = await loop.create_server(
            lambda: OcfTcpServerProtocol(self),
            '192.168.1.11', 8777)
        await server.start_serving()

