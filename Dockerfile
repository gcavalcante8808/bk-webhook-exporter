FROM pypy:3-slim-jessie
WORKDIR /usr/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.dev.txt .
RUN pip install --no-cache-dir -r requirements.dev.txt

COPY bk_webhook_prometheus /usr/src/bk_webhook_prometheus

WORKDIR /usr/src/bk_webhook_prometheus
CMD ["pypy3","app.py"]
