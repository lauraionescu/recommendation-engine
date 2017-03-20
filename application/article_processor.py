from article import Article


def process_articles(files):
    for file in files:
        article = Article(file)
        text = article.get_text()
        topic = article.get_topics()

    return (["key", "word"], [1, 0])
