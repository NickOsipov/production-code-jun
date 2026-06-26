FROM python:3.11.4-slim-bookworm

ENV APP_HOME=/app

WORKDIR $APP_HOME

# uv 
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

# venv
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync
ENV PATH="$APP_HOME/.venv/bin:$PATH"
ENV PYTHONPATH=$APP_HOME

COPY src src
COPY config config
COPY scripts scripts

ENV FLASK_APP=src/app.py

CMD ["bash", "scripts/entrypoint.sh"]