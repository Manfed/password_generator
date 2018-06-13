FROM python:3.5

RUN mkdir -p /pg

RUN pip install -U setuptools==39.2.0 pip==9.0.1

WORKDIR /pg

ADD requirements.txt requirements.txt

RUN pip install -Ur requirements.txt

ADD ./ ./

RUN pip install -U .

ENTRYPOINT password_generator.py