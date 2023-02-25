FROM python:3.11.2

WORKDIR /app


COPY requirements.txt .
COPY run_app.sh .

COPY . .

ADD main.py .

RUN python3 -m venv venv

RUN source ./venv/bin/activate

RUN pip3 install -r requirements.txt

CMD ["./run_app.sh"]
