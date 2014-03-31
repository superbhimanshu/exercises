######################################################################
# TESTING FILE                                                       #
# Author: Himanshu Verma                                             #
# Date: 03/28/2014                                                   #
######################################################################


from RetailMeNotHeader import *
from RetailMeNotFunctions import *
stopWords = open('stop_words.txt', 'r').read().split()
dealsKeyWords = set(['free', 'coupons', 'offer', 'off', 'deals', 'bogo', 'sale','save'])


##### test cases for stopwords_remove(a, stopWords) ###########
# input='', output=[]
# input=['abs', 'ab'], output=TypeError
# input=123, output=TypeError
# input= "ABCefghigkl+!@#$%^&*()", output=['abcefghigkl', '$', '%']
####################################################
def test_stopwords_remove():
    assert stopwords_remove("""ABCefghigkl+!@#$%^&*()""", stopWords)== ['abcefghigkl', '$', '%']
    assert stopwords_remove("",stopWords)==[]
    with pytest.raises(TypeError):
        stopwords_remove(['abs','ab'],stopWords)
        stopwords_remove(123,stopWords)
        stopwords_remove(['abs',123],stopWords)
        stopwords_remove()
        stopwords_remove('abc')

##### test cases for findTypeGuitar ################
# input=['classical', 'guitar'], output='classical'
# input="" or 1, output=TypeError
# input= ['abs',2], output = SystemExit
# input= ['abs',2,'guitar'], output = TypeError
# input = ['asd','hello', 'hi'], output=Guitar NOT FOUND, SystemExit exception
####################################################
def test_findTypeGuitar():
    assert findTypeGuitar(['classical', 'guitar'])=='classical'
    with pytest.raises(SystemExit):
        findTypeGuitar(['asd','hello','hi'])
        findTypeGuitar(['abs',2])
    with pytest.raises(TypeError):
        findTypeGuitar("")
        findTypeGuitar(1)
        findTypeGuitar(['abs',2,'guitar'])
        findTypeGuitar()



############## Test cases for newFeatureSet function #########
# input = "" or 3, output = TypeError
# input = ['avs',3], output= TyperError (all strings expected)
# input= ['hello','$'], output = {'lengthOfDeal':2,'keyword':False, '$Present':True, '%Present':False}
##############################################################
def test_newFeatureSet():
    assert newFeatureSet(['hello','$'],dealsKeyWords, stopWords)== {'lengthOfDeal':2,'keyword':False, '$Present':True, '%Present':False}
    with pytest.raises(TypeError):
        newFeatureSet(['avs',3],dealsKeyWords, stopWords)
        newFeatureSet("",dealsKeyWords, stopWords)
        newFeatureSet(3,dealsKeyWords, stopWords)
        newFeatureSet()
        newFeatureSet("12")
        newFeatureSet(['1','3'], dealsKeyWords)
        
