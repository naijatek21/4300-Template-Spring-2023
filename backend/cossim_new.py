from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer

def cosine_sim(query_tfidf, articles_tfidf, article_names):
    num_articles = articles_tfidf.shape[0]
    article_similarities = np.zeros(num_articles)
    query_norm = np.linalg.norm(query_tfidf.toarray())
    for i in range(num_articles):
        article_norm = np.linalg.norm(articles_tfidf[i].toarray())
        dot_product = np.dot(query_tfidf, articles_tfidf[i].T).toarray()[0][0]
        article_similarities[i] = dot_product / (query_norm * article_norm)
    
    sorted_indices = np.argsort(article_similarities)[::-1][:3]
    top_articles = [(article_names[i], article_similarities[i]) for i in sorted_indices]
    return top_articles



def rocchio(query, title, relevant, a = 1 ,b = .7,c = 1, clip= True):  
    tokenizer = RegexpTokenizer(r'\w+')
    
    query_arr = tokenizer.tokenize(query)
    title_arr = tokenizer.tokenize(title)
    set_arr = np.union1d(query_arr, title_arr)

    query_count = np.zeros(len(set_arr))
    title_count = np.zeros(len(set_arr))

    new_query = ""

    for i in range(len(query_arr)):
        if query_arr[i] in set_arr: 
            query_count[np.where(set_arr == query_arr[i])] += 1 

    for j in range(len(title_arr)):
        if title_arr[j] in set_arr: 
            title_count[np.where(set_arr == title_arr[j])] += 1 

    if relevant: 
        new_arr = np.round(a*query_count + b *title_count)
    else: 
        new_arr = np.round(a*query_count - c*title_count)
        if clip == True:
            new_arr[new_arr<0] = 0

    for k in range(len(set_arr)):
        new_query+= set_arr[k] + " "

    return new_query













