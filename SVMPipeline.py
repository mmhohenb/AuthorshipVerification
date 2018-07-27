# -*- coding: utf-8 -*
"""
Created on Mon Apr 30 09:53:09 2018

@author: Mercedes
"""
nGramFeatures = "C:/Users/Mercedes/AuthorshipVerification/nGramFeatures.py"
import os
import nGramFeatures

FeatureSet = ['Types/Tokens character 4grams','Types/Tokens character 5grams']
FeatureListPreArray = []

# Set the directory you want to start from
rootDir = 'C:/Users/Mercedes/AuthorshipVerification/pan15-authorship-verification-training-dataset-english-2015-04-19'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    #For each pair of documents, find Feature Values using module which codes features: AuthorshipVerification.py
    RawNGramValue = []

    FeatureValue = []
    for fname in fileList:
        print('\t%s' % fname)
        fullname = dirName+'/'+fname
        RawNGramValue.append(nGramFeatures.FourGramsToUniqueness(fullname))
        print(RawNGramValue)
        print(RawNGramValue[0])
    print("pause")
    print(RawNGramValue)
    
    #print(RawNGramValue[0])

"""
    if  RawNGramValue[0[0]] > RawNGramValue[1[0]]:
        FeatureValue.append(1)
    elif RawNGramValue[1[0]] < RawNGramValue[1[0]]:
        FeatureValue.append(1)
    else:
        FeatureValue.append(0)
        
    print(FeatureValue)
"""
        #FeatureValues = return()
        #FeatureListPreArray.append(FeatureValues)
        #run svm_implementation.py