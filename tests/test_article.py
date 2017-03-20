import os
import pytest

from application.article import Article


def test_it_extract_text_body_from_an_article():
    filepath = os.path.dirname(os.path.abspath(__file__)) +"/datafile.json"
    article = Article(filepath, text_keyword='content')

    assert article.get_text() == "Lorem ipsum dolor sit amet"


def test_raises_error_if_default_text_keyword_not_found():
    filepath = os.path.dirname(os.path.abspath(__file__)) +"/datafile.json"
    article = Article(filepath)

    with pytest.raises(KeyError):
        assert article.get_text()
