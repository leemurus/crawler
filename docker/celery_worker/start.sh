#!/usr/bin/env sh

celery \
  --workdir src \
  --app core \
  --broker ${CELERY_BROKER_URL} \
  --result-backend ${CELERY_RESULT_BACKEND_URL} \
  worker --loglevel=INFO