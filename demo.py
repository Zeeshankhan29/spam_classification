import pandas as pd
from spam import logger
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from nltk import tokenize
import streamlit as st
import pickle
import re
import os
import nltk

# nltk.download()


#Initializing lemmitization
lem = WordNetLemmatizer()


#loading the model
try:
    with open('rand_model','rb') as f:
        model =  pickle.load(f)
except Exception as e:
    logger.exception(str(e))
    print('something went wrong please check log')
    

#loading the tfidf object
try:
    with open('tfidf','rb') as f:
        tf =  pickle.load(f)
except Exception as e:
    logger.exception(str(e))
    print('something went wrong please check log')

#prediction function
def clean_text(text):
    text = re.sub('[^a-zA-Z0-9]' ," ",text)
    text = text.lower() # Convert to lowercase
    # text = tokenize.sent_tokenize(text)#paragraph to sentences
    # text = tokenize.word_tokenize(text[0]) # sentences to word
    text = text.split()
    text = [lem.lemmatize(word) for word in text if word not in set(stopwords.words('english'))] # Remove stopwords
    return " ".join(text)

  
try:
    st.title('Spam Classification')
    message =st.text_area('Enter your text to check : ')
    result = clean_text(message)
    result =[result]
    from sklearn.feature_extraction.text import TfidfVectorizer
    X = tf.transform(result).toarray()
except Exception as e:
    print('something went wrong please check log')
    logger.exception(str(e))
    raise(e)


#Code for prediction
Prediction = ''

#Creating a button for prediction
if st.button('Classify'):
    logger.info(f'Prediction has started for : {message}')
    result = model.predict(X)
    print(result)
    if result[0]== 0:
        Prediction = 'Not a Spam Message'
    else:
        Prediction = 'Alert!! It a Spam Message'
    logger.info(f'Prediction Result: {message} is : {Prediction}')
    st.success(Prediction)
