FROM python:3.9-alpine3.16
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 setup.py

