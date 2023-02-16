FROM python:3.7-alpine

RUN apk update \
    && apk add build-base linux-headers
ENV HOST="HOST"
ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]
