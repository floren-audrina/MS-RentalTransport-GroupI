#!/bin/bash

# Check if rabbit is up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 20
done

# Run the service
export PYTHONPATH=$(pwd)

nameko run --config config.yml transport.ada_kawan.rental_transport transport.arasya.rental_transport transport.empat_roda.rental_transport transport.jayamahe.rental_transport transport.moovby.rental_transport transport.puri.rental_transport --backdoor 3000