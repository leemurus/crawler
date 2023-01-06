FROM python:3.10-alpine AS base_layer

# Need for psycopg2
RUN apk update && apk add gcc libpq-dev musl-dev

WORKDIR /app

# Need for caching previous operations
FROM base_layer AS custom_layer
# Need for image build
ARG BUILD_COMPONENT_NAME

# Install requirements.txt
COPY ${BUILD_COMPONENT_NAME}/requirements.txt ./
RUN pip install -Ur requirements.txt

# Set start.sh file
COPY ${BUILD_COMPONENT_NAME}/start.sh ./
RUN chmod +x ./start.sh
