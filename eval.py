"""
Evaluate precision 
"""

from pymagnitude import *
import pandas as pd

def eval(eval_set, proj, target):
    num = 0
    counter = 0
    for i in range(eval_set.shape[0]):
        counter += 1
        trans = target.most_similar(proj.query(eval_set[i][0]))
        trans = [t[0].lower() for t in trans]
        if eval_set[i][1] in trans or eval_set[i][1]+'s' in trans:
            num += 1
        print('{}/{}'.format(num, counter))
    return num / len(eval_set)

if __name__=='__main__':
    train = pd.read_csv('train_dict.txt', sep=' ', header=None).values
    test = pd.read_csv('test_dict.txt', sep=' ', header=None).values
    print("### DONE LOADING DATA ###")
    proj = Magnitude('/data1/minh/dumped/debug/procrustes/vectors-wd.magnitude')
    target = Magnitude('/data1/minh/magnitude/img.magnitude')
    train_acc = eval(train, proj, target)
    test_acc = eval(test, proj, target)
    print("Train accuracy: {}, test accuracy: {}".format(train_acc, test_acc))
    
