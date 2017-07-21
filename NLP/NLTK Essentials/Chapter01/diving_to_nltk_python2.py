# -*- coding: UTF-8 -*-
# 重要：python2 必须要有上述编码声明

# python2 不用NLTK的方式，提取文本并分词

import urllib2

responses = urllib2.urlopen("http://python.org/") # 下载网页数据
html = responses.read()  # 读取网页数据（包含hmtl）
print len(html)

# tokens = [tok for tok in html.split()]   #分词
# print "Total number of tokens :"+ str(len(tokens))  #统计词数
# print tokens[0:20]  
# 除了文本内容，还含有html标签，需要再清洗，以下用re直接剥离提炼

import re

tokens = re.split("\W+", html)
print "Total number of tokens : {}".format(len(tokens))
print tokens[:20]

# 上述方式可以用nltk 实现得更简洁

# 词频统计及排序-字典按value排序
# python 方式：
import operator
freq_dis = {}
for tok in tokens:
    if tok in freq_dis:
        freq_dis[tok] += 1
    else:
        freq_dis[tok] = 1
sorted_freq_dist = sorted(freq_dis.items(), key = operator.itemgetter(1), reverse=True)
print sorted_freq_dist[:20]

# NLTK 方式：
import nltk
Freq_dist_nltk = nltk.FreqDist(tokens)
print Freq_dist_nltk
print('\n--------------')
for k, v in Freq_dist_nltk.items():
    print str(k) + ':' + str(v)

# stopwords
# stopwords = [word.strip().lower() for word in open("PATH/english.stop.txt")] # 需要停用词库
# clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopwords]
# Freq_dist_nltk = nltk.FreqDist(clean_tokens)    
# Freq_dist_nltk.plot(50, cumulative=False)