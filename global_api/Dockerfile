FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

RUN chmod +x ./scripts/manage.sh ./scripts/entrypoint.sh
ENTRYPOINT ["./scripts/entrypoint.sh"]

