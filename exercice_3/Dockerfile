FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN apt-get -y update

RUN apt-get -y install curl

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port" , "8000"]