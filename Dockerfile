FROM python:3.5

ADD . /recommendation-engine

WORKDIR recommendation-engine
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
