FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.10.8 /uv /uvx /bin/

WORKDIR /service
COPY ./app/pyproject.toml ./app/uv.lock ./
RUN uv sync --frozen --no-dev
COPY ./app ./

EXPOSE 8001

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
