from nltk.tokenize import RegexpTokenizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

def tokenizeWords(words):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(words)
def word_to_index_gen(articles):
    word_to_index = {}
    set_words = set()
    for _,article in articles.items():
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
    articles_keys = articles.keys()
    for i,key in enumerate(articles_keys):
        for j,word in enumerate((word_to_index.keys())):
            matrix[i][j] = articles[key].count(word)
    return matrix 
def cosine_sim(query_tf, articles_tf):
    article_similarities = np.zeros(len(articles_tf))
    for i,article_tf in enumerate(articles_tf):
        article_similarities[i] = (np.dot(query_tf,article_tf) /((np.linalg.norm(article_tf))  * np.linalg.norm(query_tf)))
    article_similarities[np.isnan(article_similarities)] = 0
    return article_similarities
def testing(query, articles):
    query_tf = tf_query(query,word_to_index)
    article_tf = tf_articles(articles,word_to_index)
    sim_scores = cosine_sim(query_tf,article_tf)
    recommendations = sort_top_k(sim_scores,index_titles)
def sort_top_k (article_sims, index_titles, k = 3):
    article_names = []
    sort_rankings = np.argsort(article_sims)[::-1][:k]
    for i in sort_rankings:
        article_names.append((index_titles[i],article_sims[i]))
    return article_names
def get_index_titles(article_titles):
    index_to_title = {}
    for idx, title in enumerate(article_titles):
        index_to_title[idx] = title
    return index_to_title

relevant = defaultdict(list)
irrelevant = defaultdict(list)

def update_relevant(query, title):
    print("updating relevant")
    query_toks = tokenizeWords(query)
    title_toks = tokenizeWords(title)
    for qword in query_toks:
        for tword in title_toks:
            relevant[qword] += [tword]
    print(relevant)
    return

def update_irrelevant(query, title):
    print("updating irrelevant")
    query_toks = tokenizeWords(query)
    title_toks = tokenizeWords(title)
    for qword in query_toks:
        for tword in title_toks:
            irrelevant[qword] += [tword]
    print(irrelevant)
    return