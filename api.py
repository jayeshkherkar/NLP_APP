import nlpcloud
from dotenv import load_dotenv
import os
import time
import spacy

load_dotenv()
#retriving api key
API_KEY = os.getenv("key")

def ner(text,entity):
    client = nlpcloud.Client("llama-3-1-405b",API_KEY, gpu=True)
    e1 = entity.split(",")
    l = []
    for i in range(0,len(e1)):
        l.append(client.entities(text,searched_entity=e1[i]))           
    return l

def chatbot():
    pass

def sentiment_analysis():
    pass

def translate():
    pass  
