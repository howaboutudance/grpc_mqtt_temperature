#!/usr/bin/env bash

# If the script is passed --debug, then set options for debugging
if [[ $1 == "--debug" ]]; then
    set -x
    set -e
fi

# Set environment variables
export PODMAN_NETWORK_NAME=dev-mosquitto-network
export PODMAN_POD_NAME=mosquitto-pod
export PODMAN_CONTAINER_NAME=mosquitto-broker