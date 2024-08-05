#!/usr/bin/env bash

# If the script is passed --debug, then set options for debugging
if [[ $1 == "--debug" ]]; then
    set -x
    set -e
fi


# Set the environment variables
source ./scripts/podman/env_vars.sh

# Setup network if not setup
if ! podman network inspect $PODMAN_NETWORK_NAME &> /dev/null; then
    podman network create \
    --driver bridge \
    $PODMAN_NETWORK_NAME
fi

# Setup pods
podman pod create \
    --name $PODMAN_POD_NAME \
    --network $PODMAN_NETWORK_NAME \
    -p 1883:1883 \
    -p 9001:9001

# Start the containers
podman run -d --name $PODMAN_CONTAINER_NAME \
    --pod $PODMAN_POD_NAME \
    --network $PODMAN_NETWORK_NAME \
    -p 1883:1883 \
    -p 9001:9001 \
    -v ./scripts/podman/mosquitto/data:/mosquitto/data \
    -v ./scripts/podman/mosquitto/log:/mosquitto/log \
    eclipse-mosquitto

# wait for the container to start
sleep 5