# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set an environment variable to prevent buffering of Python output
ENV PYTHONUNBUFFERED 1

# Install system packages required for the image
RUN apt-get update && apt-get install -y \
    cron \
    libpq-dev libmagic-dev gettext

# Create a non-root user inside the container
RUN addgroup --system django && adduser --system --ingroup django django

# Set the working directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $HOME $APP_HOME
WORKDIR $APP_HOME

# Copy and install Python requirements
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt && rm -rf /requirements

# Copy the entrypoint and start scripts
COPY ./compose/production/django/entrypoint /entrypoint
RUN chmod +x /entrypoint && chown django /entrypoint

COPY ./compose/production/django/start /start
RUN chmod +x /start && chown django /start

# Copy the application code
COPY --chown=django:django . $APP_HOME

# Create necessary directories and set permissions
RUN mkdir $APP_HOME/main/static && chown django $APP_HOME/main/static
RUN mkdir $APP_HOME/main/media && chown django $APP_HOME/main/media
RUN chmod gu+rw /var/run && chmod gu+s /usr/sbin/cron

# Set the user for running the container
USER django

# Specify the entrypoint command
ENTRYPOINT ["/entrypoint"]
