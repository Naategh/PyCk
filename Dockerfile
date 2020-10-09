FROM python:3.5

RUN mkdir -p /opt/pyck/
WORKDIR /opt/pyck/
COPY ./* ./
RUN pip install -r requirements.txt
