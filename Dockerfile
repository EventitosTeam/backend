FROM python:3.10-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

# RUN cd /usr/src/app/swagger_server

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]