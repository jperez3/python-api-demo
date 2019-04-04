FROM python:3.7-alpine

RUN mkdir /usr/app
ADD ./app /usr/app
WORKDIR /usr/app
RUN apk update \
    && pip3 install -r requirements.txt \
    && apk add sqlite \
    && rm -rf /var/cache/apk/* \
    && chmod +x init.sh \
    && ./init.sh

CMD ["python3","/usr/app/app.py"]