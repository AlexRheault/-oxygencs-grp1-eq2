FROM python:3.8-alpine

COPY ./libs.txt /tmp/pip-tmp/libs.txt

RUN pip --disable-pip-version-check --no-cache-dir install \
    -r /tmp/pip-tmp/libs.txt \
    && rm -rf /tmp/pip-tmp

WORKDIR /app
COPY . /app/

CMD ["python", "src/main.py"]