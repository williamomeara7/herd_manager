FROM python:3.8.10-slim

COPY . /app


WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade
RUN /opt/venv/bin/pip install -r requirements.txt


CMD ["app/entrypoint.sh"]