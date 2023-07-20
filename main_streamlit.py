import streamlit as st
import json
from random import choice
import os

def get_jsonlist():
    '''获取json文件列表'''
    files = os.listdir('.')
    s = []
    for file in files:
        if '.json' in file:
            s.append(file)
    return s

def read_articles(file_name):
    '''读入json文件'''
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

def get_input(hints):
    '''输入替换词'''
    keys = []
    for hint in hints:
        m = st.text_input(f'请输入{hint}')
        keys.append(m)
    return keys

def replace(article, keys):
    '''进行替换'''
    for i in range(len(keys)):
        article = article.replace(f'{{{{{i + 1}}}}}', f'{{{keys[i]}}}')
    return article

#文件选择
st.title("Word Filling Game")
file_name = st.selectbox("file_name:",get_jsonlist())
st.write('Please input the filename first!')

if not file_name:
    exit()

#文件内文章选择
data = read_articles(file_name)
articles = data["articles"]
m = list()
for article in articles:
    m.append(article['title'])
m.append('random')
title = st.selectbox("title:",tuple(m))

st.button('确认', on_click=click_button)
if not st.session_state.clicked:
    exit()

#获取并打出文章
if title == 'random':
    art = choice(articles)
else:
    for article in articles:
        if title == article['title']:
            art = article
st.subheader('Article')
st.write(art['article'])

#输入关键词并进行替换
hints = art['hints']
keys = get_input(hints)
if st.button('替换'):
    st.subheader('Replace')
    st.write(replace(art['article'], keys))

