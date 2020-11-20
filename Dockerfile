FROM ubuntu:18.04

WORKDIR /code

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /code

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "full_api/settings.py", "full_api:app"]
