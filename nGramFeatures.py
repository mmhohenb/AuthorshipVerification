# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:06:02 2018

@author: Mercedes

Contains scripts to find the uniqueness of ngrams in a document.
Hope: Similar Uniqueness in two documents is correlated with documents being written by same author.
"""
import re

def charFourGrams(Document):
    with open(Document) as File:
        String = File.read()
        RemoveNewLines = re.sub('\n',' ',String)
        RemoveTabs = re.sub('\t', '',RemoveNewLines)
        RemoveMultipleSpaces = re.sub('\s+',' ',RemoveTabs)
        CharacterUnigramList = []
        CharacterFourGramList = []

        for line in RemoveMultipleSpaces:
            if line:
                #print(line)
                for character in line:
                    CharacterUnigramList.append(character)
                
        InitialFourGram = "---"+RemoveMultipleSpaces[0]
        SecondFourGram = "--"+RemoveMultipleSpaces[0]+RemoveMultipleSpaces[1]
        ThirdFourGram = "-"+RemoveMultipleSpaces[0]+RemoveMultipleSpaces[1]+RemoveMultipleSpaces[2]
        
        CharacterFourGramList.append(InitialFourGram)
        CharacterFourGramList.append(SecondFourGram)
        CharacterFourGramList.append(ThirdFourGram)
        
        count = 0
        DocCharLength = len(CharacterUnigramList)

        for character in CharacterUnigramList:
            if count >= 3:
                if count < DocCharLength-1:
                    
                    CharFourGram = CharacterUnigramList[count-3]+CharacterUnigramList[count-2]+CharacterUnigramList[count-1]+CharacterUnigramList[count]
                    CharacterFourGramList.append(CharFourGram)
                    count += 1
                else:
                    File.close()
            else: 
                count += 1
        return(CharacterFourGramList)
    
def charFiveGrams(Document):
    with open(Document) as File:
        String = File.read()
        RemoveNewLines = re.sub('\n',' ',String)
        CharacterUnigramList = []
        CharacterFiveGramList = []

        for line in RemoveNewLines:
            for character in line:
                CharacterUnigramList.append(character)
                
        InitialFiveGram = "----"+RemoveNewLines[0]
        SecondFiveGram = "---"+RemoveNewLines[0]+RemoveNewLines[1]
        ThirdFiveGram = "--"+RemoveNewLines[0]+RemoveNewLines[1]+RemoveNewLines[2]
        FourthFiveGram = "-"+RemoveNewLines[0]+RemoveNewLines[1]+RemoveNewLines[2]+RemoveNewLines[3]
        
        CharacterFiveGramList.append(InitialFiveGram)
        CharacterFiveGramList.append(SecondFiveGram)
        CharacterFiveGramList.append(ThirdFiveGram)
        CharacterFiveGramList.append(FourthFiveGram)
        
        count = 0
        DocCharLength = len(CharacterUnigramList)

        for character in CharacterUnigramList:
            if count >= 4:
                if count < DocCharLength-1:
                    
                    CharFiveGram = CharacterUnigramList[count-4]+CharacterUnigramList[count-3]+CharacterUnigramList[count-2]+CharacterUnigramList[count-1]+CharacterUnigramList[count]
                    CharacterFiveGramList.append(CharFiveGram)
                    count += 1
                else:
                    File.close()
            else: 
                count += 1
        return(CharacterFiveGramList)
    
def nGramFreq(CharacterNGramList):
    nGramFreqDictionary = {}
    
    for NGram in CharacterNGramList:
        if NGram in nGramFreqDictionary:
            nGramFreqDictionary[NGram] += 1
        else:
            nGramFreqDictionary[NGram] = 1                           
    return(nGramFreqDictionary)    
    
def UniquenessProbability(FreqDictionaryOfNGrams):
    NumberOfTypes = len(FreqDictionaryOfNGrams)
    NumberOfTokens = 0

    for NGram in FreqDictionaryOfNGrams:
        NumberOfTokens = NumberOfTokens+FreqDictionaryOfNGrams[NGram] 
        
    UniquenessProbability = float(NumberOfTypes/NumberOfTokens)
    
    return(UniquenessProbability)

def FourGramsToUniqueness(sourcedocument):    
    return(UniquenessProbability(nGramFreq(charFourGrams(sourcedocument))))

def FiveGramsToUniqueness(sourcedocument):    
    return(UniquenessProbability(nGramFreq(charFiveGrams(sourcedocument))))

def nGramFeatureList(FourGramsToUniqueness,FiveGramsToUniqueness):
    FeatureList = [[FourGramsToUniqueness],[FiveGramsToUniqueness]]
    return(FeatureList)

def main() :
    print(FourGramsToUniqueness(document1))
    print(FourGramsToUniqueness(documentU))
    print(FiveGramsToUniqueness(document1))
    print(FiveGramsToUniqueness(documentU))

document1 = "C:/Users/Mercedes/Desktop/EN001/known01.txt"
documentU = "C:/Users/Mercedes/Desktop/EN001/unknown.txt"


if __name__ == "main":
    main()
