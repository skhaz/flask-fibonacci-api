FROM python:3.9-alpine AS base

ENV PATH "/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

FROM base AS builder
RUN python -m venv /opt/venv
COPY requirements requirements
RUN pip install --no-cache-dir --upgrade pip -r requirements/common.txt

FROM base AS test
WORKDIR /tests
RUN python -m venv /opt/venv
COPY requirements requirements
RUN pip install --no-cache-dir --upgrade pip -r requirements/tests.txt
COPY app app
COPY tests tests
RUN python -m pytest tests

FROM base
COPY --from=builder /opt/venv /opt/venv
COPY app/ app/

ARG PORT=5000
ENV PORT $PORT
EXPOSE $PORT
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app