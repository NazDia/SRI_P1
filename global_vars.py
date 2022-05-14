from os import getcwd, listdir
from os.path import join, isfile

doc_terms = 'doc_terms'
terms_doc = 'terms_doc'
db_path = join(getcwd(),'DB')
doc_temrs_path = join(getcwd(), doc_terms)
terms_doc_path = join(getcwd(), terms_doc)
docs_total = len([f for f in listdir(db_path) if isfile(join(db_path, f))]) - 2