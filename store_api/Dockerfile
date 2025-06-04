FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["./scripts/manage.sh", "make"]
CMD ["./scripts/manage.sh", "migrate"]
CMD ["./scripts/entrypoint.sh"]
