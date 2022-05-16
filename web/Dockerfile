FROM python:3.10.4

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY .  /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask",  "run"]