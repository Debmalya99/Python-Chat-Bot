import pickle

corpus_list = []

with open("corpus.txt","r") as text_file:
    corpus_list = text_file.readlines()

with open("corpus.bin","wb") as pickle_file:
    pickle.dump(corpus_list,pickle_file)