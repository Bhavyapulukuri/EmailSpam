#!/usr/bin/env python
# vim: set fileencoding=ISO-8859-1:
# _*_ coding: ISO-8859-1 _*_


from __future__ import print_function, division
import nltk
import random
import os
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify
#from __future__ import print_function, division

wnl = WordNetLemmatizer()
features = []


def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file,'r', encoding='ISO-8859-1')
        a_list.append(f.read())
    f.close()
    return a_list

spam = init_lists('/media/sf_EmailSpam/spam/')
ham = init_lists('/media/sf_EmailSpam/ham/')

all_emails = [(email,'spam') for email in spam]
all_emails += [(email,'ham') for email in ham]

#print(all_emails)
#print(len(all_emails))

random.shuffle(all_emails)

def preprocess(sentence):
    return[wnl.lemmatize(word.lower()) for word in word_tokenize(sentence)]

stoplist = stopwords.words('english')

def get_features(text):
    return {word: count for word,count in Counter(preprocess(text)).items() if not word in stoplist}


all_features = [(get_features(email),label) for (email,label) in all_emails]
print('collected' + str(len(all_features)) + 'feature sets')




def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    print("train  size is")
    print(train_size)
    train_set, test_set = features[:train_size], features[train_size:]
    print('Training set size = ' + str(len(train_set)) + 'emails')
    print('Test set size = ' + str(len(test_set)) + 'emails')
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier


def evaluate(train_set, test_set, classifier):
    print('Accuracy on the training set =' + str(classify.accuracy(classifier,train_set)))
    print('Accuracy of the test set = '+ str(classify.accuracy(classifier, test_set)))
    classifier.show_most_informative_features(20)




train_set, test_set, classifier = train(all_features, 0.8)




evaluate(train_set, test_set, classifier)




test_set = init_lists('/media/sf_EmailSpam/Testing/')



