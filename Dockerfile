FROM python:3.9-alpine

COPY src/main.py /usr/src/main.py

CMD ["python", "/usr/src/main.py"]
EXPOSE 8000