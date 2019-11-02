"""
Learn the basics of nlp
"""
import string
#  import random
#  import numpy as np
import nltk

def lem_tokens(tokens):
    """
    :returns : tokenized lemmed string
    """
    return [LEMMER.lemmatize(token) for token in tokens]

def lem_normalize(text):
    """
    :return : Normalized Lemmed string
    """
    return lem_tokens(nltk.word_tokenize(text.lower().translate(REMOVE_PUNCT_DICT)))

FILE = open('chatbot.txt', 'r', errors='ignore')
RAW = FILE.read()

RAW = RAW.Lower()

nltk.download('punkt')
nltk.download('wordnet')

SENT_TOKENS = nltk.sent_tokenize(RAW)
WORD_TOKENS = nltk.word_tokenize(RAW)

LEMMER = nltk.stem.WordNetLemmatizer()
REMOVE_PUNCT_DICT = dict((ord(punct), None) for punct in string.punctuation)

