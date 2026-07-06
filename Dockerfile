FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml README.md ./

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -e '.[dev]'

COPY apps ./apps
COPY packages ./packages

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

