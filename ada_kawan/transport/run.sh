#!/bin/bash

# Check if rabbit is up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 20
done

# Set PYTHONPATH to the current working directory
export PYTHONPATH=$(pwd)/application/ada_kawan/transport

nameko run --config config.yml transport.rental_transport --backdoor 3000