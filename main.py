import ui
import vectorial_system
import nltk_work
import os
import os.path as path
from global_vars import db_path

if __name__ == "__main__":
    if not path.exists(db_path):
        os.mkdir(db_path)
    nltk_work.create_doc_terms()
    ui.start_ui()
    # vectorial_system.calculate_weird_vectorial(['death', 'kill'], ['life'], ['hospital'])
