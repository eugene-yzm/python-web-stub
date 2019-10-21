FROM python:alpine3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/requirements.txt ./

RUN pip3 install -r requirements.txt

CMD [ "python3" ]
