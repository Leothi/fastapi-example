FROM ubuntu:18.04

WORKDIR /code

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY . /code

RUN pip3 install .

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "api/settings.py", "api:app"]
