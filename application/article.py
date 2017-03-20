class Article:
    def __init__(self, filename):
        with open(filename, "r") as f:
            print(f.read)

    def get_text(self):
        return ''

    def get_topics(self):
        return ''
