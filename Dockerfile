FROM python:3.5

WORKDIR /recommendation-engine
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords

ENTRYPOINT ["python3", "main_runner.py"]

ADD . /recommendation-engine
