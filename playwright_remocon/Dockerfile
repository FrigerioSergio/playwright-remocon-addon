FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

COPY script.py /app/script.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
