import json, os, re, sys

from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

from application.article_processor import process_articles

if __name__ == '__main__':

    article_path = sys.argv[1]
    text_keyword = sys.argv[2]
    topic_keyword = sys.argv[3]

    (dataset, topics) = process_articles(article_path, text_keyword, topic_keyword)

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, max_features=200, stop_words='english')

    x_train = vectorizer.fit_transform(dataset)

    cosine_similarity = linear_kernel(x_train, x_train)

    i = 0
    for root, dir, filepath in os.walk(article_path):
        for file in filepath:
            max_similarity = 0;
            best_match = 'unknown';
            j = 0

            cosine_similarity_list = cosine_similarity[i].tolist()

            while j < len(cosine_similarity_list):
                if cosine_similarity_list[j] > max_similarity and cosine_similarity_list[j] < 0.999:
                    max_similarity = cosine_similarity_list[j]
                    best_match = filepath[j]
                j += 1

            print('max similarity ', max_similarity)

            print(file + ' most similar with ' + best_match)
            i += 1
