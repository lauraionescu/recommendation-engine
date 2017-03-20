import json


class Article:
    def __init__(self, filepath, text_keyword='text'):
        self.text_keyword = text_keyword

        with open(filepath, "r") as f:
            self.data = json.load(f)

    def get_text(self):
        return self.data[self.text_keyword]

    def get_topics(self):
        return ''
