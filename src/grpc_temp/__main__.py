import logging

from grpc_temp import version
from grpc_temp.config import settings
from grpc_temp import cli
from grpc_temp.server import start_server


logging.basicConfig(level=settings.log_level.upper())
_log = logging.getLogger(__name__)

# assume running cli inferface and parse args
if settings.interface == "cli" or settings.interface is None:
    _log.info("Running CLI interface")
    # parse args
    arguments = cli.parse_args()

_log.info(f"grpc_temp version: {version}")
_log.info(f"Log level: {settings.log_level}")

# start server
start_server()
