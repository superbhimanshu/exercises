######################################################################
# Function Library                                                   #
# Author: Himanshu Verma                                             #
# Date: 03/28/2014                                                   #
######################################################################

#!/usr/apps/Python/bin/python


from RetailMeNotHeader import *
## function to remove non-informative words ##
def stopwords_remove(a,stopWords):
    if((isinstance(a,str)!=True) or (isinstance(stopWords,list)!=True)):
        raise TypeError("Invalid Input Type")
    s = string.lower(a)
    for ch in """$%""":## preserving $ and % signs ##
        s = string.replace(s,ch,' '+ch+' ')
    for ch in """!"#&()*+,-/:;<=>?@^[\\]?_'`{|}?""":
        s = string.replace(s, ch,' ')
        word_list = string.split(s)
    word_list=s.split()
    filtered_words = [t for t in word_list if t.lower() not in stopWords]
    return filtered_words

## function to find type of guitar. It returns the noun or adjective string
## that appears before the word guitar 
def findTypeGuitar(line):
    if(isinstance(line,list)!=True):
        raise TypeError("Input to findTypeGuitar must be list")
    if 'guitar' in line:
        indexOfGuitar = line.index('guitar')
    else:
        print "GUITAR NOT FOUND"
        raise SystemExit(1)
    line = nltk.pos_tag(line)
    adj_list=['JJ','JJR','JJS']
    noun_list= ['NN','NNS','NNP','NNPS']
    for i in range(indexOfGuitar-1,-1,-1):
        if((line[i][1] in adj_list) or (line[i][1] in noun_list)):
            return line[i][0]
    return ''




## feature extration function for training and classification
## takes the deals words list and important keywords list and non-informative stop words list
## returns dictionary of features
def newFeatureSet(document_words, dealsKeyWords, stopWords):
    if((isinstance(document_words,list)!=True) or (isinstance(stopWords,list)!=True)):
        raise TypeError("Invalid Input Type")
    if(isinstance(dealsKeyWords,set)!=True):
        raise TypeError("Invalid Input Type")
    
    features ={}
    document_words = ' '.join(document_words)
    word_features = stopwords_remove(document_words, stopWords)
    word_features = [stem(x) for x in word_features]
    features['lengthOfDeal'] = len(word_features)
    for term in dealsKeyWords:
        features[term]=False
#    features['keyword']=False
    features['$Present'] = False
    features['%Present']=False
    for word in word_features:
        if(word in dealsKeyWords):
            features[word]=True
#            features['keyword']=True
        if(word =='$'):
            features['$Present']=True
        if(word=='%'):
            features['%Present']=True
    return features

