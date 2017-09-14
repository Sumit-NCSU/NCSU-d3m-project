# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:58:32 2017

@author: sagargupta
"""
from textblob import TextBlob
data = open('/Users/sagargupta/Desktop/DDDM/Syndrome_AND_Rare_Disease.txt').read().decode('utf-8')
bunch = TextBlob(data)

find_good = bunch.sentences

'''
key_words = ['rare', 'disease', 'diseases', 'syndrome', 'patients', 'treatment', 'Syndrome', 'Rare', 'condition']
'''
print find_good.__len__()
technical_key_words = ['rare', 'disease', 'diseases', 'syndrome', 'patients', 'treatment', 'Syndrome', 'Rare', 'condition']
legal_key_words = ['copyrights', 'rights', 'advocacy', 'FDA', 'NORD', 'legal', 'law', 'Administrative Law', 'Law and Technology', 
                   'Legal Studies', 'Litigation', 'Risk', 'Social Sciences and the Law', 'Sociobiology and Law', 'agency', 'supervision', 'control', 
                   'approved', 'rule', 'rules', 'ordinance', 'measures', 'controls', 'regulator']
ethical_key_words = ['awareness', 'care', 'good', 'moral', 'ethical', 'morality', 'ethically', 'safe',
                     'moralistic', 'righteous', 'honorable', 'morales', 'virtue', 'civilized', 'wholesome', 'societal']
''' economical_keywords = ['cost', 'taxes] '''
fp = open('/Users/sagargupta/Desktop/DDDM/0831/sentences-legal.txt', 'w')
for sentence in find_good:
    if(any(map(lambda word: word in sentence, legal_key_words))):
        print>>fp, sentence
fp.close()