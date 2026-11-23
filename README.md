# Task API

A small JSON API for tasks, built with Flask, backed by Postgres, and orchestrated with Docker Compose. Tests run in CI on every push.

![CI](https://github.com/Mohican76/task-api/actions/workflows/ci.yml/badge.svg)

## Stack

- Flask 3 (Python 3.12)
- Postgres 16
- Docker + Docker Compose
- pytest
- GitHub Actions

## Endpoints

| Method | Path      | Description                          |
|--------|-----------|--------------------------------------|
| GET    | `/health` | Liveness check                       |
| GET    | `/tasks`  | List all tasks                       |
| POST   | `/tasks`  | Create a task (`{"title": "..."}`)   |

## Run locally

Requires Docker and Docker Compose.

```bash
docker compose up --build -d
