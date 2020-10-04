# Building stage
FROM python:3.7-slim as build-env

COPY requirements.txt ./

RUN pip3 install --upgrade pip
RUN apt-get update && \
    apt-get -y --no-install-recommends install cmake git protobuf-compiler build-essential && \
    mkdir /install && \
    pip install --prefix=/install -r requirements.txt

# Google managed image
FROM gcr.io/google-appengine/debian10

RUN apt-get update && \
    apt-get -y --no-install-recommends install python3 python3-setuptools libgeos-dev libpython3.7  && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/local/bin/python
ENV PYTHONPATH=/usr/lib/python3.7/site-packages
COPY --from=build-env /install /usr

COPY . /app
WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--timeout-keep-alive", "600"]

