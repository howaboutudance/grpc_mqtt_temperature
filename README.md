# grpc_temp: MQTT-to-gRPC Temparture Gateway

grpc_temp is a python project to take a message to bridge mqttt services
serving temperature into a gRPC API.

## Project Configuration

This project is a Python project that:

- is configured as a pyproject.toml project (does not use Poetry)
- uses `wheel` for it’s build system
- Is deployed as a Docker/OCI container

## Development Configuration

To configure for development (assuming using no IDE):

- Set your python interperter with `pyenv` to the require minimum in
  pyproject.toml
- Setup a virtulenv (`python -m venv .venv`) and activate
  (`source .venv/bin/activate`)
- Run basic unit test using tox (`tox -e dev`) to check unit test work
  correctlly
- Run the server `python -m grpc_temp` from within the `./src` folder
