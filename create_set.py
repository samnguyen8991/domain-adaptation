"""
Create train / test set for supervision
conc / abs ratio: 0.8 / 0.2 for both train / test set 
"""

import numpy as np
import pickle 

def create_set():
    with open('/data1/minh/multimodal/ratings_dict.p', 'rb') as fp:
        ratings_dict = pickle.load(fp)
    word_dict = {} # make sure the added word is unique
    # conc = True if the one-letter word has conc ratings >= 2.5
    # conc = True if the phrase contains at least one concrete word
    with open('/data1/minh/multimodal/words.txt', 'r') as f:
        for line in f:
            conc = False
            word = line.strip('\n')
            # check if this word has previously been added 
            if word in word_dict:
                continue 

            word_pr = word.split('row-')[1]
            # check if the line is a phrase
            if '_' in word_pr:
                components = word_pr.split('_')
                for c in components:
                    if c in ratings_dict and ratings_dict[c] >= 2.5:
                        conc = True 
            elif word_pr in ratings_dict and ratings_dict[word_pr] >= 2.5:
                conc = True 
            
            if conc:
                with open('conc.txt', 'a') as f:
                    f.write('{} {}\n'.format(word_pr, word))
            else:
                with open('abs.txt', 'a') as f:
                    f.write('{} {}\n'.format(word_pr, word))
            word_dict[word] = True

if __name__=='__main__':
    create_set()



        

