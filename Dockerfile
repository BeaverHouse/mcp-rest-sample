FROM python:3.12-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.11 /uv /uvx /bin/
COPY ./app ./app

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# .venv folder already exists, but it's not valid
# https://github.com/astral-sh/uv/issues/9423
RUN rm -rf .venv
RUN uv sync --frozen --no-dev --python-preference=only-system

EXPOSE 8001

ENTRYPOINT ["uv", "run", "python", "run_server.py"]
