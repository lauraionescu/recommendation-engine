from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron

class Article:
    def __init__(self):
        self.data = ["key", "word"]
        self.target = [1, 0]

def get_article_data(test=False):
    return Article()


data_train = get_article_data()
data_test = get_article_data(test=True)

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

x_train = vectorizer.fit_transform(data_train.data)
x_test = vectorizer.transform(data_test.data)
y_train = data_train.target

feature_names = vectorizer.get_feature_names()

print(feature_names)


clf = Perceptron(n_iter=50)
clf.fit(x_train, y_train)

pred = clf.predict(x_test)

print(pred)
