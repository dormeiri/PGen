FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app