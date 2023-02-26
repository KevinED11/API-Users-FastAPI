FROM python:3.11.2

WORKDIR /app

COPY . .

ENV VIRTUAL_ENV=/env

RUN python3 -m venv $VIRTUAL_ENV

RUN pip3 install -r requirements.txt

CMD ["./run_app.sh"]
