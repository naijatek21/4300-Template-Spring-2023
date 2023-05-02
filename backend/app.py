import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
import jaccard as jd
import cossim as cos
import cossim_new
from sklearn.feature_extraction.text import TfidfVectorizer

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
        data_token = results_as_dict[i]["content"].lower()
        doc_dictionary[iterator] = data_token
        iterator+=1
    return doc_dictionary

#Takes in the tuple array of top k searches from the similarity measure, and returns the top k titles of articles in an array 
def top_titles_scores(top_k_searches): 
    title_score_arr = []
    sql_article = f"""SELECT title, publication FROM mytable""" 
    data = mysql_engine.query_selector(sql_article)
    results_as_dict = data.mappings().all()
    for i in range(len(top_k_searches)):
        article_index = top_k_searches[i][0]
        score = top_k_searches[i][1]
        title_score_arr.append((results_as_dict[article_index]["title"], score, results_as_dict[article_index]["publication"]))

    return title_score_arr

def json_serializer(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    else:
        raise TypeError(
            "Unserializable object {} of type {}".format(obj, type(obj))
        )

def json_conversion(titles_score):
    keys = ["title","sim","publication"]
    return json.dumps([dict(zip(keys,i)) for i in titles_score])
    


@app.route("/")
def home():
    return render_template('index.html',title="sample html")

#Social Data
@app.route("/source")
def get_social_data():
    source = request.args.get("source")
    
    source_sql = f"""SELECT * FROM mytable2 WHERE news_source = '{source}'"""
    data = mysql_engine.query_selector(source_sql)
    results_as_dict = dict(data.mappings().all()[0])
    return json.dumps(results_as_dict, default=json_serializer)

#Search for Articles
@app.route("/titles")
def search_cossim():
    text = request.args.get("text")
    docs_dictionary = build_docs_dictionary()
    index_titles = list(docs_dictionary.keys())
    vectorizer = TfidfVectorizer()
    article_tfidf = vectorizer.fit_transform(docs_dictionary.values())
    query_tfidf = vectorizer.transform([text.lower()])
    top_articles = cossim_new.cosine_sim(query_tfidf, article_tfidf, index_titles)
    top = top_titles_scores(top_articles)
    return json_conversion(top)
    
#Send Rocchio Feedback
@app.route("/feedback")
def send_feedback():
    query = request.args.get("query")
    title = request.args.get("title")
    relevant = request.args.get("relevant")

    cos.update_rocchio_dict(query, title, relevant == "true")

    return json.dumps({}, default=json_serializer)