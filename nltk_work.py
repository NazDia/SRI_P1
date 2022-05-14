import json
from os import listdir
from os.path import isfile, join
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from global_vars import doc_temrs_path, db_path, doc_terms, terms_doc, terms_doc_path

stemmer = SnowballStemmer('english')
noun_tags = ['NN', 'NNP', 'NNS', 'NNPS']

def get_from_doc(path):
    fd = open(path, 'r', encoding='utf8', errors='ignore')
    print(path)
    text = fd.read()
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    ret = pos_tag([stemmer.stem(x[0]) for x in tags if x[1] in noun_tags])
    fd.close()
    return ret

def create_doc_terms(forced=False):
    try:
        fd = open(doc_temrs_path, 'r')
        try:
            dic = json.load(fd)
        except:
            dic = {}

    except:
        fd = open(doc_temrs_path, 'x')
        dic = {}

    fd.close()
    
    try:
        fd = open(terms_doc_path, 'r')
        try:
            dic2 = json.load(fd)
        except:
            dic2 = {}

    except:
        fd = open(terms_doc_path, 'x')
        dic2 = {}

    fd.close()

    files = [f for f in listdir(db_path) if isfile(join(db_path, f)) and f != doc_terms and f != terms_doc]
    change = False
    for f in files:
        try:
            if not forced:
                dic[f]
            else:
                change = True
                temp = get_from_doc(join(db_path, f))
                dic[f] = {}
                for i, _ in temp:
                    try:
                        dic[f][i] += 1
                    except KeyError:
                        dic[f][i]  = 1

        except KeyError:
            change = True
            temp = get_from_doc(join(db_path, f))
            dic[f] = {}
            for i, _ in temp:
                try:
                    dic[f][i] += 1
                except KeyError:
                    dic[f][i]  = 1
        
        for w in dic[f]:
            try:
                dic2[w].append(f)
            except KeyError:
                dic2[w] = [f]

    if change:
        fd = open(doc_temrs_path, 'w')
        json.dump(dic, fd)
        fd.close()
        fd = open(terms_doc_path, 'w')
        json.dump(dic2, fd)
        fd.close()

if __name__ == "__main__":
    create_doc_terms()