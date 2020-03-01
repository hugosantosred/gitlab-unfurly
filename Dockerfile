FROM python:3.6

# update apt-get
RUN apt-get update -y && apt-get upgrade -y

RUN mkdir -p app
WORKDIR app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 app:app
