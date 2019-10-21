FROM python:alpine3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 5000

WORKDIR /app

COPY * /app/

RUN pip3 install -r requirements.txt

CMD [ "python3",  "main.py" ]
