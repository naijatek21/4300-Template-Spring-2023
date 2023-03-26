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

term_dict = {0: ["There", "dog"], 1: ["Hello"], 2: ["Hi", "Hi", "the"], 3: ["There", "There"], 4: ["Hi", "There"]}
print(jaccard(["Hi", "There"], term_dict))
print(sort_top_k(jaccard(["Hi", "There"], term_dict)))
