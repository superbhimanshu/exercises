##""" Groups and Topics

##The objective of this task is to explore the structure of the deals.txt file. 

##Building on task 1, we now want to start to understand the relationships to help us understand:

##1. What groups exist within the deals?
##2. What topics exist within the deals?

##"""
######################################################################
# Topic Modeling By LDA                                              #
# Author: Himanshu Verma                                             #
# Date: 03/27/2014
######################################################################

##########################################################################
## In this implementaion we use LDA for Topic Modeling ###################
## Topics can be considered as groups while words associated with them####
## can be considered specific field or topic as per test's requirement####
##########################################################################

from RetailMeNotHeader import *
from RetailMeNotFunctions import *

goodDealList=[] ## list of all good deals ##
allTopics=[] ## list of all topics generated by LDA technique ##
goodDeals = open('../data/deals.txt', 'r')
stopWords = open('../data/stop_words.txt', 'r').read().split()

for line in goodDeals:
    goodDealList.append(line)

fullText=[stopwords_remove(document,stopWords) for document in goodDealList]
dictionary = corpora.Dictionary(fullText)
corpus = [dictionary.doc2bow(text) for text in fullText]
tfidf = models.TfidfModel(corpus) ## Estimation of term frequency inverse document frequency statistic ##
corpusTfidf = tfidf[corpus]
numberOfTopics = 5  ## Number of topics we want to estimate ##
lda = models.LdaModel(corpusTfidf, id2word=dictionary, num_topics=numberOfTopics)

for i in range(0, numberOfTopics):
    temp = lda.show_topic(i, 10)## to find 10 most contributing words to the topic ##
    terms = []
    for term in temp:
        terms.append(term[1])
    allTopics.append(terms)
    print "terms for topic  " + str(i) +  '  '+ ", ".join(terms) ### for debugging

 
print 'Topics Probability ' + str(lda[corpus[1]])
print 'Most Probable Topic: ' + str(max(lda[corpus[1]],key=itemgetter(1))[0])
