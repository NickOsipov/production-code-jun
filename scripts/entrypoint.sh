#!/bin/bash

if [ "$MODE_ENV" = "dev" ]; then
    echo "Running in development mode"
    tail -f /dev/null
else
    echo "Running in production mode"
    python3 src/pipeline.py
    flask run --host=0.0.0.0 --port=5000
fi

