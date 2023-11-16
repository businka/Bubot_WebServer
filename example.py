import logging
from buject.OcfDevice.subtype.WebServer.WebServer import WebServer


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s %(name)s.%(funcName)s %(message)s'
    )
    device = WebServer.init_from_file()
    device.run()
