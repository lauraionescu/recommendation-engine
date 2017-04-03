import os

from application import article_processor as article_processor


def test_process_articles_extracts_topics_from_fileset():
    filespath = os.path.dirname(os.path.abspath(__file__)) +"/data"
    content, topics = article_processor.process_articles(filespath, text_keyword='content', topics_keyword='keywords')

    assert ["history", "vowels", "dummy"] in topics
    assert ["history", "latin", "dummy"] in topics


def test_process_articles_extracts_text_from_fileset():
    filespath = os.path.dirname(os.path.abspath(__file__)) +"/data"
    content, topics = article_processor.process_articles(filespath, text_keyword='content', topics_keyword='keywords')

    assert "cow" in content[0]
    assert "is" not in content[0]
