import os

from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from bs4 import BeautifulSoup

from application.article import Article


def process_articles(filepath, text_keyword='text', topics_keyword='topics'):
    content = []
    topics = []

    for root, dir, filelist in os.walk(filepath):
        for file in filelist:
            article = Article(filepath + '/' + file, text_keyword, topics_keyword)
            text = article.get_text()
            topic = article.get_topics()
            content.append(strip_stopwords(text))
            topics.append(topic)

    return (content, topics)


def strip_stopwords(raw_text):
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = [stemmer.stem(w) for w in tokenizer.tokenize(raw_text.lower()) if w not in set(stopwords.words('english'))]
    raw_text = ' '.join(tokens)
    return raw_text


def strip_html(raw_text):
    return BeautifulSoup(raw_text.replace('&nbsp;', ''), 'html.parser').get_text()


if __name__ == '__main__':
    import sys
    process_articles(sys.argv[1], 'body', 'channel_ids')
