ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt-get update

COPY ./libs.txt /tmp/pip-tmp/libs.txt

RUN pip --disable-pip-version-check --no-cache-dir install \
    -r /tmp/pip-tmp/libs.txt \
    && rm -rf /tmp/pip-tmp