FROM python:3-alpine

RUN mkdir -p /home/data
RUN mkdir -p /home/output

WORKDIR /usr/src/app

COPY main.py ./main.py

CMD [ "python", "./main.py"]
