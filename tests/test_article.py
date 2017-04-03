import os
import pytest

from application.article import Article


FILEPATH = os.path.dirname(os.path.abspath(__file__)) +"/data/datafile.json"

def test_it_extracts_text_body_from_an_article():
    article = Article(FILEPATH, text_keyword='content')

    assert article.get_text() == "Lorem ipsum dolor sit amet"


def test_raises_error_if_default_text_keyword_not_found():
    article = Article(FILEPATH)

    with pytest.raises(KeyError):
        assert article.get_text()


def test_it_extracts_topics_from_an_article():
    article = Article(FILEPATH, topics_keyword='keywords')
    expected_topics = ["history", "latin", "dummy"]

    retrieved_topics = article.get_topics()

    assert len(retrieved_topics) == 3
    for t in expected_topics:
        assert t in retrieved_topics


def test_raises_error_if_default_topic_keyword_not_found():
    article = Article(FILEPATH)

    with pytest.raises(KeyError):
        assert article.get_topics()
