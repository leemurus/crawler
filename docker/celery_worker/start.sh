#!/usr/bin/env sh

celery \
  --workdir src \
  --app core \
  worker --loglevel=INFO