FROM python:3.7.6-slim
WORKDIR /

RUN apt-get -y update \
  && pip install --upgrade pip
  
COPY . /
RUN pip install -r /requirements.txt
ENTRYPOINT ["python", "train.py"]