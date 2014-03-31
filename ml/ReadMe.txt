FILES DESCRIPTION:-

------------------Code Files--------------
1. RetailMeNotHeader.py - All required imports are mentioned in this file
2. RetailMeNotFunctions.py - This is the function library
3. test_RetailMeNotFunctions.py - This file can be used for testing, It has testing scenarios for the functions 
(using py.test filename command) 
4. task1.py - Solution to Task1 has been implemented in this file. Here is the glimpse of output. More detailed 
              output is presented in RetailMeNot

ANSWERS:-
-Words Frequency Distribution has been implemented- RetailMeNotWordsDistribution.png shows the most frequent 
terms used accross all the deals.
Ascending order of word frequency distribution has been saved in RetailMeNotWordsDistributionData.txt to access 
lowest frequent terms and for further processing. This file can also be used for implementing caching for faster 
analysis when new data comes. 

5. task2.py- Topic modeling using LDA technique has been done in this file as per requirements. 
             Topics are the groups in the project's nomenclature. 
             Most informative words are the topics in the project's nomenclature.

6. task3.py - 

Attempt 1:
----------
Defined number of topics to be 4. Topic modeling using LDA was implemented and most informative words from the 
most probable topic were selected as keywords. These keywords were added to another list of predefined keywords 
like "deals","offer", "coupons", "save", "bogo" etc. Implemented classification algorithm using naive bayesian 
classifier, feature extractor with four defined features(length of data, $ sign is present or not, % sign is 
present or not, keyword present or not) and classifier evaluator(Precision, Recall and F-Test).

ANSWERS:-
Accuracy :  0.8
Most Informative Features
                $Present = True             good : bad    =      2.6 : 1.0
                %Present = True             good : bad    =      2.6 : 1.0
                 keyword = True             good : bad    =      2.4 : 1.0
                 keyword = False             bad : good   =      1.6 : 1.0
good precision: 0.875
good recall: 0.7
good F-measure: 0.777777777778
bad precision: 0.75
bad recall: 0.9
bad F-measure: 0.818181818182

Our classifier is not very general because we used feature extractor specific to short text and features related 
to deals only(Predifined keywords were used).It will need more tuning if data form changes to long texts as more
features can be extracted because of extra information.
Classification can surely be improved by increasing the amount of training data. Moreover, if we can increase 
the number of relevant features it will surely enhance the performance.

Attempt 2 Increasing Features.
-----------------------------
Decreased the number of topics to 2. And 50 most informative words were selected from the most probable topic. 
These words were added to a predefined keywords list. After stemming each word is considered as a feature. Here 
is the outcome.
Most Informative Features
                %Present = True             good : bad    =      2.4 : 1.0
                       % = True             good : bad    =      2.4 : 1.0
            lengthOfDeal = 6                good : bad    =      2.0 : 1.0
                    shop = True             good : bad    =      1.3 : 1.0
good precision: 0.75
good recall: 0.529411764706
good F-measure: 0.620689655172
bad precision: 0.714285714286
bad recall: 0.869565217391
bad F-measure: 0.78431372549


Our classifier is not very general because we used feature extractor specific to short text and features related
to deals only. It will need more tuning if data form changes to long texts as more features can be extracted because
of extra information. Classification can surely be improved by increasing the amount of training data. Moreover, 
if we can increase the number of relevant features it will surely enhance the performance.
Word Sense Disambiguation can be implemented to find the proper context of each word present in the data and we can  
estimate the closeness of the words with keywords like "deals", "offer" and "percentage off" etc.

Attempt 3 Tuning features again:-
---------------------------------
Decreased the number of topics to 2. And 50 most informative words were selected from the most probable topic. 
After stemming each word is considered as a feature. This time no predefined keyword list was used. Here is the outcome.

Accuracy :  0.9
Most Informative Features
            lengthOfDeal = 6                good : bad    =      2.1 : 1.0
                $Present = True             good : bad    =      2.1 : 1.0
                %Present = True             good : bad    =      1.9 : 1.0
                %Present = False             bad : good   =      1.2 : 1.0
good precision: 0.904761904762
good recall: 0.904761904762
good F-measure: 0.904761904762
bad precision: 0.894736842105
bad recall: 0.894736842105
bad F-measure: 0.894736842105

We can clearly see the improvement in classification. This time our classifier in quite general as we didnt use 
any predefined keyword list and all the features are extracted computationally. So this can be used on any problem 
statement.
