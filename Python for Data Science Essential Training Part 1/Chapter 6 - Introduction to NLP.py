import nltk
nltk.download('stopwords')

text = "On Wednesday, the Association for Computing Machinery, the world’s largest society of computing professionals, announced that Hinton, LeCun and Bengio had won this year’s Turing Award for their work on neural networks. The Turing Award, which was introduced in 1966, is often called the Nobel Prize of computing, and it includes a $1 million prize, which the three scientists will share."

nltk.download('punkt')


## Sentence Tokenizer
from nltk.tokenize import sent_tokenize
sent_tk = sent_tokenize(text)
print("Sentence tokenizing the text: \n")
print(sent_tk)

## Word Tokenizer
from nltk.tokenize import word_tokenize
word_tk = word_tokenize(text)
print("Word tokenizing the text: \n")
print(word_tk)

## Removing Stop Words (words that don't add specific value)
from nltk.corpus import stopwords
sw = set(stopwords.words("English"))
print("stop words in English language are: \n")
print(sw)
filtered_words = [w for w in word_tk if not w in sw]
print("The text after removing stopwords \n:")
print(filtered_words)

## Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

port_stem = PorterStemmer()
stemmed_words = []

for w in filtered_words:
    stemmed_words.append(port_stem.stem(w))

print("Filtered Sentence: \n", filtered_words, '\n')

print('Stemmed sentence: \n', stemmed_words)

## Lemmatizing
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()
lemm_words = []

for i in range(len(filtered_words)):
    lemm_words.append(lem.lemmatize(filtered_words[i]))

print(lemm_words)

## Parts of Speech Tagging
nltk.download("averaged_perceptron_tagger")
from nltk import pos_tag
pos_tagged_words = pos_tag(word_tk)
print(pos_tagged_words)

## Frequency Distribution Plots
from nltk.probability import FreqDist
fd = FreqDist(word_tk)
##print(fd)

import matplotlib.pyplot as plt
fd.plot(30, cumulative=False)
plt.show()

fd_alpha = FreqDist(text)
fd_alpha.plot(30, cumulative=False)
