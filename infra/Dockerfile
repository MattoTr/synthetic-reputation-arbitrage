FROM python:3.11-slim

WORKDIR /app

COPY ../src ./src
COPY ../scripts ./scripts
COPY ../secrets ./secrets
COPY ../tests ./tests
COPY ../README.md ./

RUN pip install -r src/requirements.txt

CMD ["python", "scripts/start_local.py"]
