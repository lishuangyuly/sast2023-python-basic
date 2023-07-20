import argparse
import json
from random import choice


def parse_data():
    parser = argparse.ArgumentParser(
        prog='Word Filling Game',
        description='A simple game',
        allow_abbrev=True
    )
    parser.add_argument('--file', '-f', help='the path of file', required=True)
    parser.add_argument('--article','-a', help='choose the article you like')
    args = parser.parse_args()
    return args

def read_articles(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_input(hints):
    keys =[]
    for hint in hints:
        m = input(f'请输入{hint}')
        keys.append(m)
    return keys

def replace(article, keys):
    for i in range(len(keys)):
        article = article.replace(f'{{{{{i + 1}}}}}', f'{{{keys[i]}}}')
    return article

if __name__ == "__main__":
    args = parse_data()
    data = read_articles(args.file)
    articles = data["articles"]
    if args.article:
        for article in articles:
            if args.article == article['title']:
                art = article
    else:
        art = choice(articles)

    keys = get_input(art['hints'])
    fin = art['article']
    print(replace(fin, keys))
    
