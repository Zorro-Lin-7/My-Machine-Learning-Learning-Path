# -*- coding: UTF-8 -*-
# python3

import requests
from bs4 import BeautifulSoup
import re

web_data = requests.get("http://python.org/") # get 整个网页元数据
python_html = web_data.text                # 元数据中提取html部分的文本
soup = BeautifulSoup(python_html,'lxml')     # 解析html文本，好比 混合物状态的汤 变成 分层的汤
clean = soup.get_text()   #从“分层”的汤里，提取“html文本”这一层 
# print(clean)
tokens = [tok for tok in clean.split()]
print("Total number of tokens: {}".format(len(tokens)))
print(tokens[:25])
print("\n---------------")
# 对比：用re貌似提纯度更高,也可能分词更细导致噪音增加
tokens_by_re = re.split("\W+", clean)
print("Total number of tokens_by_re: {}".format(len(tokens_by_re)))
print(tokens_by_re[:25])

import nltk
Freq_dist_nltk = nltk.FreqDist(tokens)  # 词频统计
print(Freq_dist_nltk)
print("\n------------")
for k, v in Freq_dist_nltk.items():
    print(str(k) + ':' + str(v))

# stopwords exist
Freq_dist_nltk.plot(50, cumulative=False)

# no stopwords
# stopwords = [word.strip().lower() for word in open("PATH/english.stop.txt")]
# clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopwords)]
# Freq_dist_nltk = nltk.FreqDist(clean_tokens)
# Freq_dist_nltk.plot(50, cumulative=False)
