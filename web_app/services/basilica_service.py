# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("BASILICA_API_KEY")
print("---------")

connection = basilica.Connection(API_KEY)
print(type(connection)) #> <class 'basilica.Connection'>
print("---------")

sentence = "Hello again"
sent_embeddings = connection.embed_sentence(sentence)
print(list(sent_embeddings))
print("---------")

sentences = ["Hello world!", "How are you?"]
print(sentences)

embeddings = connection.embed_sentences(sentences)
print("EMBEDDINGS...")
print(type(embeddings))
print(list(embeddings)) # [[0.8556405305862427, ...], ...]