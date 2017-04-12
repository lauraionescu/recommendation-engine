import os, sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from application.article_processor import process_articles


def write_best_three(article_path, similarity, filename):
    i = 0
    for root, dr, filepath in os.walk(article_path):
        for file in filepath:
            best_matches = [];
            similarity_list = similarity[i].tolist()
            best_three = sorted(similarity_list)[-4:-1]

            j = 0
            while j < len(similarity_list):
                if similarity_list[j] in best_three and similarity_list[j] > 0:
                    best_matches.append(filepath[j])
                j += 1

            with (open(filename, "a")) as f:
                f.write('max similarity: \n')
                for b in best_three:
                    f.write(str(b))
                    f.write('\n')

                f.write('\n')

                f.write(file + ' most similar with: \n')
                for m in best_matches:
                    f.write(m)
                    f.write('\n')

                f.write('\n')

                f.write('.......................................')
                f.write('\n')
            i += 1


if __name__ == '__main__':

    article_path = sys.argv[1]
    text_keyword = sys.argv[2]
    topic_keyword = sys.argv[3]
    results_file = sys.argv[4]

    (dataset, topics) = process_articles(article_path, text_keyword, topic_keyword)

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, max_features=200, stop_words='english')

    x_train = vectorizer.fit_transform(dataset)

    similarity = linear_kernel(x_train, x_train)

    write_best_three(article_path, similarity, results_file)