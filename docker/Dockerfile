FROM python:3.10-slim AS base_layer

# It's cratch, because docker-compose can pass only args to image building
ARG DEFAULT_USER
ARG DEFAULT_USER_GROUP
ENV DEFAULT_USER ${DEFAULT_USER}
ENV DEFAULT_USER_GROUP ${DEFAULT_USER_GROUP}

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# -r create system group or user
# -g name of group for adding user
# -m create home directory
# -d overrides the default home directory location
# -s sets the login shell for the user
RUN groupadd -r ${DEFAULT_USER_GROUP} && \
    useradd -r -d /home/myuser/ -s /bin/sh -m -g ${DEFAULT_USER_GROUP} ${DEFAULT_USER}

WORKDIR /app

# --------------------------------------------------- #

# Need for caching previous operations
FROM base_layer AS custom_layer

# Need for image build
ARG BUILD_COMPONENT_NAME

# Install requirements.txt
COPY ${BUILD_COMPONENT_NAME}/requirements.txt ./
RUN pip install -Ur requirements.txt

# Set start.sh file
COPY ${BUILD_COMPONENT_NAME}/start.sh ./
RUN chmod u+x start.sh && \
    chown ${DEFAULT_USER}:${DEFAULT_USER_GROUP} start.sh
