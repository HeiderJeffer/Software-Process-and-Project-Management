############################################################
# Dockerfile to run a Django-based web application
############################################################

FROM python:2.7

# Set the file maintainer (your name - the file's author)
MAINTAINER Aleksandar Nedelchev

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=emse-sppm
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/emse-sppm


# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir media static logs
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Install Python dependencies
RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt
RUN pip install gunicorn
RUN pip install --upgrade requests

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY docker/docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]


ENTRYPOINT ["/docker-entrypoint.sh"]
