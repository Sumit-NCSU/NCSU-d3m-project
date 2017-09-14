from sklearn.feature_extraction.text import CountVectorizer
import nltk
from operator import itemgetter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
intake = open('/home/sumit/nltk/data/poopy').read()
words = word_tokenize(intake)
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(words)
idf = vectorizer.idf_
d = dict(zip(vectorizer.get_feature_names(), idf))
print(sorted(d.items(), key=itemgetter(1), reverse=True))

#print (dict(zip(vectorizer.get_feature_names(), idf)))
#print(intake)
