from nltk.tokenize import RegexpTokenizer


def tokenizeWords(words):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(words)


# query_terms is tokenized string of distinct terms for the input, and doc_terms is tokenized string for a document


def jaccard (query_terms, doc_terms):
    doc_similarities = []
    for k, v in doc_terms.items():
        numerator = set(query_terms).intersection(set(v))
        denominator = set(query_terms).union(set(v))
        doc_similarities.append((k,len(numerator)/len(denominator)))

    return doc_similarities






def sort_top_k (doc_sims, k = 3):
    sort_rankings = sorted(doc_sims, key = lambda x: x[1], reverse = True)
    return sort_rankings[:k]



#Test Case 1:
print("#### TEST CASE 1 ####")
term_dict = {0: ["There", "dog"], 1: ["Hello"], 2: ["Hi", "Hi", "the"], 3: ["There", "There"], 4: ["Hi", "There"]}
print(jaccard(["Hi", "There"], term_dict))
print(sort_top_k(jaccard(["Hi", "There"], term_dict)))

#Test Case 2: 
print("#### TEST CASE 2 ####")
term_dict2 = {0: [], 1:["Hi","There", "Everyone"], 2: ["Hi"] , 3: []}
print(jaccard(["Hi", "There"], term_dict2))
print(sort_top_k(jaccard(["Hi", "There"], term_dict2)))

#Test Case 3:
print("#### TEST CASE 3 ####")
term_dict3 = {0: ["Hello"], 1:["Hi","There", "Everyone"], 2: ["Hi"] , 3: [], 4: ["Hello", "World"]}
print(jaccard(["Hello"], term_dict3))
print(sort_top_k(jaccard(["Hello"], term_dict3)))

#Test Case 4:
print("#### TEST CASE 4 ####")
term_dict4 = {0: ["Hey"], 1: ["There", "Hey"]   , 2:  [],  3:[]   , 4: ["ey", "Hey"]  , 5: ["Hey","There", "Friend"]}
print(jaccard(["Hey", "There", "Friend"], term_dict4))
print(sort_top_k(jaccard(["Hey", "There", "Friend"], term_dict4)))

#Test Case 5:
print("#### TEST CASE 5 ####")
term_dict5 = {0: [], 1: [], 2: [], 3:[]}
print(jaccard(["Hey", "There", "Friend"], term_dict5))
print(sort_top_k(jaccard(["Hey", "There", "Friend"], term_dict5)))
