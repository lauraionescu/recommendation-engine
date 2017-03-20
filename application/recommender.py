from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron

from article_processor import process_articles

def get_article_data(test=False):
    return process_articles([])

train_data, train_target = get_article_data()
test_data, _ = get_article_data(test=True)

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

x_train = vectorizer.fit_transform(train_data)
x_test = vectorizer.transform(test_data)
y_train = train_target

feature_names = vectorizer.get_feature_names()

print(feature_names)

clf = Perceptron(n_iter=50)
clf.fit(x_train, y_train)

pred = clf.predict(x_test)

print(pred)
