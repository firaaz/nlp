"""
Learn the basics of nlp
"""
import string
#  import random
#  import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer # convert raw doc to matrix to TF-IDF
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

def main():
    """
    Main control flow of the program
    """
    def lem_normalize(text):
        """
        :return : Normalized Lemmed string
        """
        return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    def lem_tokens(tokens):
        """
        :returns : tokenized lemmed string
        """
        return [lemmer.lemmatize(token) for token in tokens]

    def greeting(sentence):
        for word in sentence.split():
            if word.lower() in GREETING_INPUT:
                return random.choice(GREETING_RESPONSES)

    def response(user_response):
        robo_response = ''
        sent_tokens.append(user_response)

        TfidfVec = TfidfVectorizer(tokenizer=lem_normalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)

        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfid = flat[-2]

        if req_tfid == 0:
            robo_response = robo_response + 'I am sorry! I dont undertand you'
        else:
            robo_response = robo_response + sent_tokens[idx]

        return robo_response

    file = open('chatbot.txt', 'r', errors='ignore')

    raw = file.read()
    raw = raw.lower()

    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)

    lemmer = nltk.stem.WordNetLemmatizer()
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    GREETING_INPUT = ("hello", "hi", "greetings", "sup", "what's up", "hey")
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello"]

    flag = True
    print("""ROBO: My name is Robo, I will anwer your queries about chatbots.
If you want to exit, type Bye!""")

    while flag == True:
        user_response = input("> ")
        user_response = user_response.lower()

        if user_response != 'bye':
            if user_response in ('thanks', 'thank you'):
                flag = False

                print("ROBO: You are welcome")

            else:
                if(greeting(user_response) != None):
                    print("ROBO: " + greeting(user_response))
                else:
                    print("ROBO: " + response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            print("ROBO: Bye! take care")

if __name__ == "__main__":
    main()
