import json


class Article:
    def __init__(self, filepath, text_keyword='text', topics_keyword='topics'):
        self.text_keyword = text_keyword
        self.topics_keyword = topics_keyword

        with open(filepath, "r") as f:
            self.data = json.load(f)

    def get_text(self):
        return self.data[self.text_keyword]

    def get_topics(self):
        return self.data[self.topics_keyword]
