FROM python:3.7-alpine

RUN mkdir /usr/app
ADD ./app /usr/app
WORKDIR /usr/app
RUN pip3 install -r requirements.txt

CMD ["/bin/ash"]