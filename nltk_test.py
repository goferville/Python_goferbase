import nltk
import requests, lxml

text=" Hello everyone. Hope all are fine and doing well. Hope you find the book interesting. Ami a Gofer? Yes, I'm."

from nltk.tokenize import sent_tokenize
#
print('Into sentence')
print(sent_tokenize(text))
print('Into sentence')
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
print(tokenizer.tokenize(text))
print('Into words')
print(nltk.word_tokenize(text))

r=requests.get('http://www.wenxuecity.com/news/2018/07/28/7478474.html')
text=(r.text)

print(text)
print('---------------------------------------')
print(nltk.word_tokenize(text))
#print(r.history)