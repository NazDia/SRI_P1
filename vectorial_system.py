import math
import json
import numpy as np
from os import listdir
from os.path import isfile, join
from global_vars import doc_temrs_path, db_path, docs_total, terms_doc_path, doc_terms, terms_doc


def calculate_weird_vectorial(words, less_important, banned_words):
    q_vector = [1 if x in words else 0.5 for x in words + less_important]
    subtotal, banned = get_subtotal(banned_words)
    fd = open(terms_doc_path, 'r')
    dic = json.load(fd)
    fd.close()
    idf_l = [calculate_idf([y for y in dic[x] if y in subtotal] if x in dic else [], subtotal) for x in words + less_important]
    fd = open(doc_temrs_path, 'r')
    dic = json.load(fd)
    fd.close()
    tf_l = { doc : [calculate_tf(x, doc, dic) for x in words + less_important] for doc in subtotal }
    w_ij = { doc : [tf_l[doc][j] * idf_l[j] for j in range(len(tf_l[doc]))] for doc in tf_l }
    vals = { doc : np.dot(q_vector, tf_l[doc]) / (np.linalg.norm(q_vector) * np.linalg.norm(tf_l[doc])) for doc in tf_l if not math.isnan(np.dot(q_vector, tf_l[doc]) / (np.linalg.norm(q_vector) * np.linalg.norm(tf_l[doc]))) }
    ret = {}
    for i in vals:
        try:
            ret[vals[i]].append(i)
        except KeyError:
            ret[vals[i]] = [i]

    return ret

def get_subtotal(banned_words):
    fd = open(terms_doc_path, 'r')
    dic = json.load(fd)
    fd.close()
    banned_docs = []
    for i in banned_words:
        try:
            for j in dic[i]:
                if not j in banned_docs:
                    banned_docs.append(j)

        except KeyError:
            pass

    return [f for f in listdir(db_path) if isfile(join(db_path, f)) and not f in banned_docs and f != doc_terms and f != terms_doc], banned_docs

def calculate_idf(list, subtotal):
    if len(list) == 0:
        return 0
    return math.log((float)(len(subtotal))/ (float)(len(list)), (float)(len(subtotal)))

def calculate_tf(word, doc, dic):
    max_freq = 0
    for w in dic[doc]:
        if dic[doc][w] > max_freq:
            max_freq = dic[doc][w]

    try:
        ret = dic[doc][word] / (dic[doc][word] * max_freq)
    except KeyError:
        ret = 0

    return ret
