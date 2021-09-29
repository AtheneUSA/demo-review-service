#!/bin/sh

set -e

. /venv/bin/activate

exec uvicorn --host 0.0.0.0 --port 8000 review_service.main:app
