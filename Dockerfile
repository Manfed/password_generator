FROM python:3.5

RUN mkdir -p /pg

RUN python3 -m pip install -U setuptools==39.2.0 pip==10.0.1

WORKDIR /pg

ADD requirements.txt requirements.txt

RUN python3 -m pip install -Ur requirements.txt

ADD ./ ./

RUN python3 -m pip install -U .

ENV DATABASE_FILE /pg/words.txt

ENV GMAIL_PASSWORD secret

EXPOSE 8080

ENTRYPOINT start_generator.py