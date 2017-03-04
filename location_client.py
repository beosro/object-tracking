import logging
import socket
import time
from threading import Event

import grpc
from gen.grpc_server_pb2 import ClientInfo
from gen.grpc_server_pb2 import ObjectLocationServerStub
from grpc_support import GenericClient
from grpc_support import TimeoutException

logger = logging.getLogger(__name__)

class LocationClient(GenericClient):
    def __init__(self, hostname):
        super(LocationClient, self).__init__(hostname, "location client")
        self.__x_ready = Event()
        self.__y_ready = Event()
        self.__id = -1
        self.__x = -1
        self.__y = -1
        self.__width = -1
        self.__height = -1
        self.__middle_inc = -1

    def _mark_ready(self):
        self.__x_ready.set()
        self.__y_ready.set()

    def _get_values(self, pause_secs=2.0):
        channel = grpc.insecure_channel(self._hostname)
        stub = ObjectLocationServerStub(channel)
        while not self.stopped:
            logger.info("Connecting to gRPC server at {0}...".format(self._hostname))
            try:
                client_info = ClientInfo(info="{0} client".format(socket.gethostname()))
                server_info = stub.registerClient(client_info)
            except BaseException as e:
                logger.error("Failed to connect to gRPC server at {0} [{1}]".format(self._hostname, e))
                time.sleep(pause_secs)
                continue

            logger.info("Connected to gRPC server at {0} [{1}]".format(self._hostname, server_info.info))

            try:
                for val in stub.getObjectLocations(client_info):
                    with self.value_lock:
                        self.__id = val.id
                        self.__x = val.x
                        self.__y = val.y
                        self.__width = val.width
                        self.__height = val.height
                        self.__middle_inc = val.middle_inc
                    self._mark_ready()
            except BaseException as e:
                logger.info("Disconnected from gRPC server at {0} [{1}]".format(self._hostname, e))
                time.sleep(pause_secs)

    # Non-blocking
    def get_loc(self, name):
        return self.__x if name == "x" else self.__y

    # Non-blocking
    def get_size(self, name):
        return self.__width if name == "x" else self.__height

    # Blocking
    def get_x(self, timeout=None):
        while not self.stopped:
            if not self.__x_ready.wait(timeout):
                raise TimeoutException
            with self.value_lock:
                if self.__x_ready.is_set() and not self.stopped:
                    self.__x_ready.clear()
                    return self.__x, self.__width, self.__middle_inc, self.__id

    # Blocking
    def get_y(self, timeout=None):
        while not self.stopped:
            if not self.__y_ready.wait(timeout):
                raise TimeoutException
            with self.value_lock:
                if self.__y_ready.is_set() and not self.stopped:
                    self.__y_ready.clear()
                    return self.__y, self.__height, self.__middle_inc, self.__id

    # Blocking
    def get_xy(self):
        return self.get_x(), self.get_y()
