import os

from application import article_processor as article_processor


def test_process_articles_extracts_topics_from_fileset():
    filespath = os.path.dirname(os.path.abspath(__file__)) +"/data"
    content, topics = article_processor.process_articles(filespath, text_keyword='content', topics_keyword='keywords')

    assert ["history", "vowels", "dummy"] in topics
    assert ["history", "latin", "dummy"] in topics


def test_process_articles_extracts_optional_topics_from_fileset():
    filespath = os.path.dirname(os.path.abspath(__file__)) +"/data"
    content, topics = article_processor.process_articles(filespath,
                                                        text_keyword='content',
                                                        topics_keyword='keywords',
                                                        optional_fields=['year', 'author'])

    print(content[0])
    assert "Elocution" in content[0]
    assert "1926" in content[0]


def test_process_articles_extracts_text_from_fileset():
    filespath = os.path.dirname(os.path.abspath(__file__)) +"/data"
    content, topics = article_processor.process_articles(filespath, text_keyword='content', topics_keyword='keywords')

    assert "cow" in content[0]
    assert "is" not in content[0]


def test_strip_html_removes_html_tags_from_text():
    raw_text = "<html><h1>fantastic python and where to find it<p>&nbsp;</h1><img src='hello.png'/>Hi</html>"

    assert article_processor.strip_html(raw_text) == "fantastic python and where to find itHi"
