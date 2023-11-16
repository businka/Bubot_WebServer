import asyncio


class OcfTcpClientProtocol(asyncio.Protocol):
    # def __init__(self, server):
    #     super().__init__()
    #     self.transport = None
    #     self.server = server

    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)
