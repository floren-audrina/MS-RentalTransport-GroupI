#!/bin/bash

# Check if rabbit is up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 2
done

# Run Service

nameko run --config config.yml gateway.gateway gateway.gateway1 gateway.gateway2 gateway.gateway3 gateway.gateway4 gateway.gateway5 --backdoor 3000