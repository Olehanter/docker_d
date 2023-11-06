FROM python:3.10-slim

WORKDIR /app/

ADD main.py main2.py

CMD python3 main2.py


