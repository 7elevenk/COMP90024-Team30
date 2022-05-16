FROM python:3

ADD . /

RUN pip install -r requirements.txt

FROM ubuntu

COPY ["./run_harv.sh", "/"]

RUN chmod +x /run_harv.sh

ENTRYPOINT ["/run_harv.sh"]
