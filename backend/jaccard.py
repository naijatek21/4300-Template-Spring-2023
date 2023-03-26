from nltk.tokenize import RegexpTokenizer


def tokenizeWords(words):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(words)


# query_terms is tokenized string of distinct terms for the input, and doc_terms is tokenized string of distinct terms for a document


def jaccard (query_terms, doc_terms):
    doc_similarities = []
    for k, v in doc_terms.items():
        numerator = set(query_terms).intersection(set(v))
        denominator = set(query_terms).union(set(v))
        doc_similarities.append((k,len(numerator)/len(denominator)))

    return doc_similarities


#query_terms is a tokenized string (include non-distinct terms) for the input, and doc_terms is a tokenized string (include non-distinct terms)
def jaccard_generalized (query_terms, doc_terms): 
    doc_similarities = []
    for k, v in doc_terms.items():
        numerator = 0
        denominator = 0
        combined = query_terms + v
        set_combined = list(set(combined))
        for i in set_combined:
            term_count_query = query_terms.count(i)
            term_count_doc = v.count(i)
            numerator += min(term_count_query, term_count_doc)
            denominator += max(term_count_query, term_count_doc)
        
        doc_similarities.append((k , numerator/denominator))
    
    return doc_similarities

#sort top k tuples of scores and doc_ids
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


term_dict6 = {0: ["Hey"], 1: ["There", "Hey"]   , 2:  ["Hey", "Hey", "There", "There"],  3:["Friend", "Friend"]   , 4: ["ey", "Hey"]  , 5: ["Hey","There", "Friend"]}
print(jaccard_generalized(["Hey", "There", "Friend"], term_dict6))