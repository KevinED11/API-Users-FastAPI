FROM python:3.11.2

WORKDIR /nutrition-app

COPY requirements.txt .

ADD backend/main.py .

RUN pip3 install -r requirements.txt

COPY backend/main.py .

CMD ["python3", "./main.py"]
