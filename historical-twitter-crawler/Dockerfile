FROM python:3

ADD . /

RUN pip install -r requirements.txt


FROM ubuntu

COPY ["./run_import_historical.sh", "/"]

RUN chmod +x /run_import_historical.sh

ENTRYPOINT ["/run_import_historical.sh"]


FROM python:3

RUN chmod +x /historical_create_view.py

CMD["python", "./historical_create_view.py"]
