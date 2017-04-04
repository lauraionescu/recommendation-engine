import os, sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from application.article_processor import process_articles

if __name__ == '__main__':

    article_path = sys.argv[1]
    text_keyword = sys.argv[2]
    topic_keyword = sys.argv[3]

    (dataset, topics) = process_articles(article_path, text_keyword, topic_keyword)

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, max_features=200, stop_words='english')

    x_train = vectorizer.fit_transform(dataset)

    similarity = linear_kernel(x_train, x_train)

    i = 0
    for root, dir, filepath in os.walk(article_path):
        for file in filepath:
            max_similarity = 0;
            best_matches = [];
            j = 0

            similarity_list = similarity[i].tolist()
            best_three = sorted(similarity_list)[-4:-1]

            while j < len(similarity_list):
                if similarity_list[j] in best_three and similarity_list[j] > 0:
                    best_matches.append(filepath[j])
                j += 1

            print('max similarity ')
            print(best_three)

            print(file + ' most similar with ')
            print(best_matches)
            i += 1
            print('.......................................')
