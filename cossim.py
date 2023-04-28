from nltk.tokenize import RegexpTokenizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

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

# def testing(query, articles):
#     query_tf = tf_query(query,word_to_index)
#     article_tf = tf_articles(articles,word_to_index)
#     sim_scores = cosine_sim(query_tf,article_tf)
#     recommendations = sort_top_k(sim_scores,index_titles)
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


def update_relevant(query, title):
    return

def update_irrelevant(query, title):
    return

relevant = {
    "house": ["biden","crisis"],
    "town":["ghost"],
    "ukraine":['russia','biden']
}

irrelevant = {
    "biggest": ["biden", "sport","ball"],
    "russia":["trump"]
} 
def rocchio(query, relevant, irrelevant, articles, word_to_index,a=.6, b=.3, c=.6, clip = True):
    q1 = 0
    q0 = query
    dr = []
    dnr = []
    for i, word in enumerate(word_to_index.keys()):
        if query[word_to_index[word]] > 0:
            dr_row = np.zeros(len(q0))
            dnr_row = np.zeros(len(q0))
            if len(relevant) > 0 and relevant.get(word) is not None:
                for i in relevant.get(word):
                    if word_to_index.get(i) is not None:
                        dr_row[word_to_index[i]] += 1 
            if len(irrelevant) > 0 and irrelevant.get(word) is not None:
                for i in irrelevant.get(word):
                    if word_to_index.get(i) is not None:
                        dnr_row[word_to_index[i]] += 1 
            if sum(dr_row) != 0:
                dr.append(dr_row)
            if sum(dnr_row) != 0:
                dnr.append(dnr_row)
    dr = np.zeros((2,len(q0))) if dr == [] else dr
    dnr = np.zeros((2,len(q0))) if dnr == [] else dnr
    q1 = (a*q0 + (b*np.mean(np.array(dr), axis = 0)) - (b*np.mean(np.array(dnr), axis = 0)))
    if clip:
        q1[q1<0] = 0
    return q1

# # prepocessing
# # TEST CASE 1
# tie: with rocchio we no longer have a tie because it considered more relevant words
print("test 1")
query =['white', 'house','biden', 'biden']
articles = {0:["the", "white","house"], 1:["war", "in","ukraine"],2:["biggest", "housing","crisis"],3:["the", "upcomming","election"],4:["trump", "and","biden"]}
index_titles = list(articles.keys())
word_to_index = word_to_index_gen(articles)
query_tf = tf_query(query,word_to_index)
article_tf = tf_articles(articles,word_to_index)
new_query = rocchio(query_tf, relevant, irrelevant, article_tf, word_to_index, clip = True)
sim_scores = cosine_sim(new_query,article_tf)
recommendations = sort_top_k(sim_scores,index_titles)
print(recommendations)


# TEST CASE 2
# differnt size article tf
print("test 2")
query =['white','house','trump','ukraine']
articles = {0:[], 1:["war", "in","ukraine"],2:["biggest", "house","crisis"],3:["the","election"],4:["trump"]}
index_titles = list(articles.keys())
word_to_index = word_to_index_gen(articles)
query_tf = tf_query(query,word_to_index)
article_tf = tf_articles(articles,word_to_index)
new_query = rocchio(query_tf, relevant, irrelevant, article_tf, word_to_index,clip = True)
sim_scores = cosine_sim(new_query,article_tf)
recommendations = sort_top_k(sim_scores,index_titles)
print(recommendations)


# TEST CASE 3
# one word query
print("test 3")
query =['ukraine']
articles = {0:["russia"], 1:["war", "in","ukraine"],2:["biggest", "housing","crisis","biden"],3:["the","election"],4:["trump"]}
index_titles = list(articles.keys())
word_to_index = word_to_index_gen(articles)
query_tf = tf_query(query,word_to_index)
article_tf = tf_articles(articles,word_to_index)
new_query = rocchio(query_tf, relevant, irrelevant, article_tf, word_to_index, clip = True)
sim_scores = cosine_sim(new_query,article_tf)
recommendations = sort_top_k(sim_scores,index_titles)
print(recommendations)


# # TEST CASE 4
# query not found
print("test 4")
query =['ghost']
articles = {0:["war", "in","ukraine"],1:["biggest", "housing","crisis"],2:["the","election"],3:["trump"]}
index_titles = list(articles.keys())
word_to_index = word_to_index_gen(articles)
query_tf = tf_query(query,word_to_index)
article_tf = tf_articles(articles,word_to_index)
new_query = rocchio(query_tf, relevant, irrelevant, article_tf, word_to_index, clip = True)
sim_scores = cosine_sim(new_query,article_tf)
recommendations = sort_top_k(sim_scores,index_titles)
print(recommendations)



# # TEST CASE 5
# # query word length larger than articles
print("test 5")
query =['ghost','town','war','trump','biden','russia']
articles = {0:[], 1:["war", "in","ukraine"],2:["biggest", "housing","crisis"],3:["the","election"],4:["trump"]}
index_titles = list(articles.keys())
word_to_index = word_to_index_gen(articles)
query_tf = tf_query(query,word_to_index)
article_tf = tf_articles(articles,word_to_index)
new_query = rocchio(query_tf, relevant, irrelevant, article_tf, word_to_index,clip = True)
sim_scores = cosine_sim(new_query,article_tf)
recommendations = sort_top_k(sim_scores,index_titles)
print(recommendations)

# inverted index may be needed later  
# def build_inverted_index(articles):
#     terms = {}
#     for idx in range(len(articles)) :
#         for word in set(articles[idx]):
#             if (terms.get(word)) is None:
#                 terms[word] = {idx:(articles[idx].count(word))}
#             else:
#                 terms.get(word)[idx] = articles[idx].count(word)
#     print(terms)
#     terms = list(sorted(terms.items(), key = lambda x:x[0]))
#     return terms
