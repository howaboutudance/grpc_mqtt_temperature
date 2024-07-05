import logging

from concurrent.futures import ThreadPoolExecutor

import grpc

from grpc_temp.protos import temperature_pb2_grpc as temperature_grpc
from grpc_temp.protos import temperature_pb2 as temperature_core
from grpc_temp.config import settings

_log = logging.getLogger(__name__)

class Temperature(temperature_grpc.TemperatureServiceServicer):
    def GetTemperature(self, request, context):
        _log.info(f"Received request for device {request.device_id}")
        temperature = temperature_core.Temperature()
        temperature.device_id = request.device_id
        temperature.value = 25.0
        temperature.timestamp = "2021-09-01T12:00:00Z"
        return temperature_core.GetTemperatureResponse(temperature=temperature)

def start_server():
    server = grpc.server(ThreadPoolExecutor())
    temperature_grpc.add_TemperatureServiceServicer_to_server(Temperature(), server)
    server.add_insecure_port(f"{settings.server.address}:{settings.server.port}")
    server.start()
    _log.info("Server started")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    start_server()