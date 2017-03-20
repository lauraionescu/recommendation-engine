class Article:
    def __init__(self):
        self.data, self.target = self.extract_data()

    def extract_data(self):
        return (["key", "word"], [1, 0])
