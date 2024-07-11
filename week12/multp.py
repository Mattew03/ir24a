from multiprocessing import Process, Pool
import time
from random import randrange
import numpy as np
import pandas as pd
from gensim import api


def f(x):
    #time.sleep(randrange(0,1))
    return x*x

def generate_word2vec_embeddings(text):
    emmbeddings = []
    tokens = text.lower().split()
    word_vectors = [word2vec_model[word]for word in tokens if word in word2vec_model]
    if word_vectors:
        emmbeddings.append(np.mean(word_vectors, axis=0))
    else:
            emmbeddings.append(np.zeros(word2vec_model.vector_size))
    return np.array(emmbeddings)
    

def mq(x):
    for i in range(10):
        if x[i] < x[i-1]:
            print('False')

def print10(x):
    print(x[:100])
if __name__ == '__main__':
        word2vec_model = api.load("word2vec-google-news-300")
        df = pd.read_csv('D:\U\7. Septimo\RI\ir24a\week11\data\podcastdata_dataset.csv')
        corpus = df['text']

        pool = Pool(processes=4)
        embeddings = pool.map(generate_word2vec_embeddings, corpus[:4])
        print(embeddings)
        df['embeddings'] = embeddings

        df.to_csv('D:\U\7. Septimo\RI\ir24a\week11\data\podcastdata_embeddings.csv', index=False)