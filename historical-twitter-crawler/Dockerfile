FROM python:3

ADD . /

RUN pip install -r requirements.txt


FROM ubuntu

COPY ["./run_import_historical.sh", "/"]

RUN chmod +x /run_import_historical.sh

ENTRYPOINT ["/run_import_historical.sh"]


FROM python:3

CMD ["python", "./historical_create_view.py"]
