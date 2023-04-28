import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
import jaccard as jd
import cossim as cos

# ROOT_PATH for linking with all your files. 
# Feel free to use a config.py or settings.py with a global export variable
os.environ['ROOT_PATH'] = os.path.abspath(os.path.join("..",os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
MYSQL_USER = "root"
MYSQL_USER_PASSWORD = ""
MYSQL_PORT = 3306
MYSQL_DATABASE = "fullnewsdb"

mysql_engine = MySQLDatabaseHandler(MYSQL_USER,MYSQL_USER_PASSWORD,MYSQL_PORT,MYSQL_DATABASE)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

# Sample search, the LIKE operator in this case is hard-coded, 
# but if you decide to use SQLAlchemy ORM framework, 
# there's a much better and cleaner way to do this

def build_docs_dictionary():
    doc_dictionary = {}
    iterator = 0
    query_sql = f"""SELECT content FROM mytable"""
    data = mysql_engine.query_selector(query_sql)
    results_as_dict = data.mappings().all()
    for i in range(len(results_as_dict)): 
        data_token = jd.tokenizeWords(results_as_dict[i]["content"].lower())
        doc_dictionary[iterator] = data_token
        iterator+=1
    return doc_dictionary

#Takes in the tuple array of top k searches from the similarity measure, and returns the top k titles of articles in an array 
def top_titles_scores(top_k_searches): 
    title_score_arr = []
    sql_article = f"""SELECT title FROM mytable""" 
    data = mysql_engine.query_selector(sql_article)
    results_as_dict = data.mappings().all()
    for i in range(len(top_k_searches)):
        article_index = top_k_searches[i][0]
        score = top_k_searches[i][1]
        title_score_arr.append((results_as_dict[article_index]["title"], score))
        
    return title_score_arr

def json_conversion(titles_score):
    keys = ["title","sim"]
    return json.dumps([dict(zip(keys,i)) for i in titles_score])

def json_serializer(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    else:
        raise TypeError(
            "Unserializable object {} of type {}".format(obj, type(obj))
        )


@app.route("/")
def home():
    return render_template('index.html',title="sample html")

# @app.route("/episodes")
# def episodes_search():
#     text = request.args.get("text")
#     return sql_search(text)


@app.route("/source")
def get_social_data():
    query_sql = f"""SELECT * FROM mytable2 WHERE news_source = 'Breitbart' """
    data = mysql_engine.query_selector(query_sql)
    results_as_dict = dict(data.mappings().all()[0])
    return json.dumps(results_as_dict, default=json_serializer)


# Implementing routing for Jaccard search here
@app.route("/titles")
def search_cossim():
    text = request.args.get("text")
    title = request.args.get("title")
    tokenized = cos.tokenizeWords(text.lower())
    docs_dictionary = build_docs_dictionary()
    index_titles = list(docs_dictionary.keys())
    word_to_index = cos.word_to_index_gen(docs_dictionary)
    query_tf = cos.tf_query(tokenized ,word_to_index)
    article_tf = cos.tf_articles(docs_dictionary,word_to_index)
    sim_scores = cos.cosine_sim(query_tf,article_tf)
    top_titles = cos.sort_top_k(sim_scores,index_titles)
    top = top_titles_scores(top_titles)
    social = get_social_data()
    return json_conversion(top)

# def search_jaccard():
#     text = request.args.get("text")
#     tokenized = jd.tokenizeWords(text.lower())
#     docs_dictionary = build_docs_dictionary()
#     search_similarities = jd.jaccard_generalized(tokenized, docs_dictionary)
#     top_searches = jd.sort_top_k(search_similarities)
#     top_titles = jaccard_top_titles(top_searches)
#     print(top_titles)
#     return json_conversion(top_titles)



#app.run(debug=True)


# def sql_search(episode):
#     query_sql = f"""SELECT * FROM episodes WHERE LOWER( title ) LIKE '%%{episode.lower()}%%' limit 10"""
#     keys = ["title","sim"]
#     data = mysql_engine.query_selector(query_sql)
#     print(data)
#     return json.dumps([dict(zip(keys,i)) for i in data])
