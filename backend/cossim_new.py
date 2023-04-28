from collections import defaultdict
import numpy as np



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





