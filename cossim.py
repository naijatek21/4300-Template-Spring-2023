from nltk.tokenize import RegexpTokenizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tokenizeWords(words):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(words)
def word_to_index_gen(articles):
    word_to_index = {}
    set_words = set()
    for article in articles:
        for word in article:
            set_words.add(word)
    for idx, word in enumerate(sorted(set_words)):
        word_to_index[word] = idx
    return word_to_index

def tf_query(query,word_to_index):
    matrix = np.zeros(len(word_to_index))
    for i,word in enumerate((word_to_index.keys())):
        matrix[i] = query.count(word)
    return matrix 
def tf_articles(articles,word_to_index):
    matrix = np.zeros((len(articles),len(word_to_index)))
    for i,article in enumerate(articles):
        for j,word in enumerate((word_to_index.keys())):
            matrix[i][j] = article.count(word)
    return matrix 

def cosine_sim (query_tf, articles_tf):
    article_similarities = []
    for article_tf in articles_tf:
        article_similarities.append(np.dot(query_tf,article_tf) / ((np.linalg.norm(article_tf)  * np.linalg.norm(query_tf))) )
    return article_similarities

def sort_top_k (article_sims, index_names, k = 3):
    sort_rankings = np.argsort(article_sims)[::-1][:k]
    print(sort_rankings)
    article_names = [index_names[i] for i in sort_rankings]
    return article_names
index_names = {
0:"article_one",
1:"article_two",
2:"article_three",
3:"article_four",
4:"article_five"
}
