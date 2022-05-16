FROM ubuntu

ADD . /

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip install -r requirements.txt

COPY ["./run_import_historical.sh", "/"]

RUN chmod +x /run_import_historical.sh

ENTRYPOINT ["/run_import_historical.sh"]

