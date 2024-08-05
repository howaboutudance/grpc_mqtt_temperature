#!/usr/bin/env bash

# If the script is passed --debug, then set options for debugging
if [[ $1 == "--debug" ]]; then
    set -x
    set -e
fi

# Set the environment variables
source ./scripts/podman/env_vars.sh

# Stop the container
echo "Stopping the container $PODMAN_CONTAINER_NAME..."
podman stop $PODMAN_CONTAINER_NAME
sleep 2

# Remove the container
echo "Removing the container $PODMAN_CONTAINER_NAME..."
podman rm $PODMAN_CONTAINER_NAME
sleep 2

# Remove the pod
echo "Removing the pod $PODMAN_POD_NAME"
podman pod rm $PODMAN_POD_NAME

if [[ $1 == "--all" ]]; then
    # Remove the network
    echo "Removing the network $PODMAN_NETWORK_NAME"
    podman network rm $PODMAN_NETWORK_NAME
fi

echo "Finished..."