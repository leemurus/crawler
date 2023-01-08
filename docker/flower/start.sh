#!/usr/bin/env sh

celery \
  --workdir src \
  --app core \
  flower --port=${FLOWER_PORT}