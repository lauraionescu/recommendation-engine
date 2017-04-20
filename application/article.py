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

    def get_optional_fields(self, option_list):
        extra_fields = []
        
        for o in option_list:
            option_item = self.data[o]
            if isinstance(option_item, str):
                extra_fields.append(option_item)
            else:
                [extra_fields.append(d) for d in option_item]

        return ' '.join(extra_fields)
