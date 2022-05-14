import streamlit as st
import json
from os.path import join
from vectorial_system import calculate_weird_vectorial
from global_vars import terms_doc_path, doc_temrs_path, db_path

s_words = []
li_words = []
b_words = []
preview_s = 0

def start_ui():
    st.title('Proyecto de Sistema de Recuperacion de Informacion')
    st.text('Damian O\'Hallorans Toleco C-512')
    st.header('Recuperacion de documentos')
    all_words = get_all_words()
    key_words()
    less_important_words()
    banned_words()
    ret = calculate_weird_vectorial(s_words, li_words, b_words)
    keys_2 = sorted(list(ret.keys()))
    keys_2.reverse()
    ret2 = []
    count = 0
    for i in keys_2:
        for elem in ret[i]:
            ret2.append(elem)
            count += 1
            if count >= 10:
                break
        if count >= 10:
            break

    display_list(ret2)

def display_list(elems):
    global preview_s
    to_show = False
    st.header('Results:')
    count = 0
    for i in elems:
        st.text(i)

    st.subheader('Documents preview')
    preview_s = st.selectbox('', elems)
    if st.button('Preview'):
        to_show = True
    if st.button('Download'):
        pass
    if to_show and preview_s in elems:
        fd = open(join(db_path, preview_s), 'r')
        text = fd.read()
        fd.close()
        st.text(text)

def key_words():
    global s_words
    c_words = st.text_input('Palabras clave')
    if st.button('Add', key='Add1'):
        s_words.append(c_words)
    if st.button('Delete in Pos', key='Delete in Pos1'):
        try:
            s_words.remove(s_words[int(c_words)])
        except:
            pass
    if st.button('Delete Word', key='Delete Word1'):
        try:
            s_words.remove(c_words)
        except:
            pass
    if st.button('Reset query', key='Reset query1'):
        s_words = []

    st.text(s_words)

def less_important_words():
    global li_words
    c_words = st.text_input('Palabras de menor importancia')
    if st.button('Add', key='Add2'):
        li_words.append(c_words)
    if st.button('Delete in Pos', key='Delete in Pos2'):
        try:
            li_words.remove(li_words[int(c_words)])
        except:
            pass
    if st.button('Delete Word', key='Delete Word2'):
        try:
            li_words.remove(c_words)
        except:
            pass
    if st.button('Reset query', key='Reset query2'):
        li_words = []

    st.text(li_words)

def banned_words():
    global b_words
    c_words = st.text_input('Palabras excluidas en los resultados')
    if st.button('Add', key='Add3'):
        b_words.append(c_words)
    if st.button('Delete in Pos', key='Delete in Pos3'):
        try:
            b_words.remove(b_words[int(c_words)])
        except:
            pass
    if st.button('Delete Word', key='Delete Word3'):
        try:
            b_words.remove(c_words)
        except:
            pass
    if st.button('Reset query', key='Reset query3'):
        b_words = []

    st.text(b_words)



def get_consult(words):
    pass

def get_all_words():
    fd = open(terms_doc_path, 'r')
    dic = json.load(fd)
    fd.close()
    return list(dic.keys())

def get_words_from_ui():
    pass

