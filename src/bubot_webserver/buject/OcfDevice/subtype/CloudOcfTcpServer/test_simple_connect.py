from unittest import IsolatedAsyncioTestCase
from .CloudOcfTcpServer import CloudOcfTcpServer
from .CloudOcfTcpClient import CloudOcfTcpClient

class TestCloudOcfTcpServer:
    async def test_1(self):
        server = CloudOcfTcpServer()
        await server.start_ocf_tcp_server()
        client1 = CloudOcfTcpClient()
        client2 = CloudOcfTcpClient()
