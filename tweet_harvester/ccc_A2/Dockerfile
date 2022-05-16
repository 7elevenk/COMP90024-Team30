FROM ubuntu:latest

ADD . /

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip install -r requirements.txt

COPY ["./run_harv.sh", "/"]

RUN chmod +x /run_harv.sh

ENTRYPOINT ["/run_harv.sh"]
