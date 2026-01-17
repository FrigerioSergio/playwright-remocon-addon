FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

COPY script.py .
COPY run.sh .

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
