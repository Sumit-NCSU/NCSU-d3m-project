#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:53:23 2017

@author: sagargupta
"""

import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords





stop_words = set(stopwords.words('english'))

data = open('/Users/sagargupta/Desktop/DDDM/Syndrome_AND_Rare_Disease.txt').read().decode('utf-8')

words = word_tokenize(data)
words_selected = []
for w in words:
    if w not in stop_words:
        words_selected.append(w)


'''
  with open('/Users/sagargupta/Desktop/DDDM/test1.txt', 'w') as f:
    print words 
    print f
'''
f = open('/Users/sagargupta/Desktop/DDDM/0831/words.txt', 'w')
for item in words:
  print>>f, item.encode('utf-8')
f.close()

f2 = open('/Users/sagargupta/Desktop/DDDM/0831/words_selected.txt', 'w')
for item in words_selected:
  print>>f2, item.encode('utf-8')
f2.close()

#   print(words_selected)
#print(words)

#apply stats to words selected