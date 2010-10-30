from __future__ import division
"""
Created on 25/10/2010

@author: peter
"""
import nltk, matplotlib, random, re
from nltk.corpus import names
from nltk.classify import apply_features

def genderFeatures1(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}
    
def genderFeatures2(word):
    return {'suffix1': word[-1:],
            'prefix1': word[0]}
    
def genderFeatures3(word):
    return {'suffix1': word[-1:],
            'prefix1': word[0],
            'suffix2': word[-2:]}
    
def genderFeatures4(word):
    return {'suffix1': word[-1],
            'prefix1': word[0],
            'prefix2': word[1],
            'suffix2': word[-2]}
    
def genderFeatures5(word):
    word = word.lower()
    return {'prefix1': word[0],
            'prefix2': word[1],
            'prefix3': word[2] if len(word) > 2 else '.' ,
            'suffix1': word[-1],
            'suffix2': word[-2],
            'suffix3': word[-3] if len(word) > 2 else '.' ,
            'length': len(word)}
    
def getMatch(compiled_pattern, word): 
    m = compiled_pattern.search(word.lower())
    return m.group() if m else ' '
       
compiled_repeated_char = re.compile(r'(\w)(\1+)')
compiled_repeated_pattern = re.compile(r'(.{1-5})(\1+)')
compiled_vowel_pair = re.compile(r'[aeiou]{2}')
compiled_consonant_pair = re.compile(r'[^aeiou]^aeiou]')
compiled_vowel_consonant_vowel = re.compile(r'[aeiou][^aeiou][aeiou]')
compiled_vowel_consonant_vowel_end = re.compile(r'.+[aeiou][^aeiou][aeiou]$')
compiled_consonant_vowel_consonant = re.compile(r'[^aeiou][aeiou][^aeiou]')
compiled_consonant2_vowel2_consonant = re.compile(r'[^aeiou]{2}[aeiou]{2}[^aeiou]')
compiled_vowel2_consonant = re.compile(r'[aeiou]{2}[^aeiou]')
compiled_vowel_both_ends = re.compile(r'^[aeiou].+[aeiou]$')
compiled_endsy = re.compile(r'.+(ie|[iy])$')
compiled_trim_endsy = re.compile(r'(.+)(ie|[iy])$')

def trimmedName(compiled_pattern, word):
    w = word.lower()
    m = compiled_pattern.search(w)
    if m and m.groups():
        return m.groups()[0]
    return w

if False:
    for word in ['Hello', 'Emmy', 'Llamb', 'Albert  Jones']:
        print word, '"' + getRepeatedChars(word) + '"'
    exit()

def genderFeatures6(word_in):
    word = word_in.lower()
    return {'prefix1': word[0],
            'repeated.chars': getMatch(compiled_repeated_char, word),
            'repeated.patterns': getMatch(compiled_repeated_pattern, word),
            'vcv': getMatch(compiled_vowel_consonant_vowel, word),
            'vcv.end': getMatch(compiled_vowel_consonant_vowel_end, word),
            'cvc': getMatch(compiled_consonant_vowel_consonant, word),
            'v2': getMatch(compiled_vowel_pair, word),
            'c2': getMatch(compiled_consonant_pair, word),
            'v_v': getMatch(compiled_vowel_both_ends, word),
            'is.endsy': getMatch(compiled_endsy, word),
            'sans.endsy': trimmedName(compiled_trim_endsy, word),
            'prefix2': word[2] if len(word) > 2 else '.' ,
            'suffix1': word[-1],
            'suffix2': word[-2],
            #'suffix3': word[-3] if len(word) > 2 else '.' ,
            'length': len(word)}
 
def genderFeatures7(word_in):
    word = word_in.lower()
    suffix1 = word[-1]
    suffix2 = word[-2]
    if suffix1 == 'a' or suffix1 == 'k':
        word = word[:-1]
    return {'prefix1': word[0],
            'repeated.chars': getMatch(compiled_repeated_char, word),
            #'repeated.patterns': getMatch(compiled_repeated_pattern, word),
            'vcv': getMatch(compiled_vowel_consonant_vowel, word),
            'vcv.end': getMatch(compiled_vowel_consonant_vowel_end, word),
            'cvc': getMatch(compiled_consonant_vowel_consonant, word),
            'v2': getMatch(compiled_vowel_pair, word),
            'c2': getMatch(compiled_consonant_pair, word),
            'v_v': getMatch(compiled_vowel_both_ends, word),
            'is.endsy': getMatch(compiled_endsy, word),
            'sans.endsy': trimmedName(compiled_trim_endsy, word),
            'suffix1': suffix1,
            #'suffix2': suffix2,
            #'suffix3': word[-3] if len(word) > 2 else '.' ,
            'length': len(word)}
    
def genderFeatures8(word_in):
    word = word_in.lower()
    suffix1 = word[-1]
    suffix2 = word[-2]
    if suffix1 in 'akfvpdmor':
        word = word[:-1]
    return {'cvc': getMatch(compiled_consonant_vowel_consonant, word),
            'suffix1': suffix1 } 
    
def genderFeatures9(word_in):
    word = word_in.lower()
    suffix1 = word[-1]
    suffix2 = word[-2:]
    suffix2a = '.'
    prefix2 = word[:2]

    if suffix1 in 'akf':
        word = word[:-1]
        suffix2 = '.'
        suffix2a = word[-2:]
    return {'prefix2': prefix2,
            'suffix1': suffix1,
            'suffix2': suffix2,
            'suffix2a': suffix2a,
            'cvc': getMatch(compiled_consonant_vowel_consonant, word),
            'c2v2c': getMatch(compiled_consonant2_vowel2_consonant, word),
            'v2c': getMatch(compiled_vowel2_consonant, word),
            
            #'v_v': getMatch(compiled_vowel_both_ends, word),
            #'v2': getMatch(compiled_vowel_pair, word),
            'repeated.chars': getMatch(compiled_repeated_char, word),
            #'vcv': getMatch(compiled_vowel_consonant_vowel, word)
            }     
   
def genderFeatures(word):
    return genderFeatures9(word)

the_names = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
the_males = ['Daniel', 'Theo', 'Vinny', 'Wallie', 'Willie',  'Wally', 'Sean', 'Tim', 'Chris']
the_females = ['Judith', 'Maddy', 'Judith', 'Lindy','Cammy', 'Chrisy', 'Clare','Tammie',
                'Grace', 'Jackie', 'Jan', 'Angie', 'Patsy','Tammy', 'Simone']
the_names = [(n,'male' if n in the_males else g) for (n,g) in the_names] 
the_names = [(n,'female' if n in the_females else g) for (n,g) in the_names] 

gender_dict = {}
for (n,g) in the_names:
    gender_dict[n.lower()] = g 

def getNames():
    global the_names
    random.shuffle(the_names)
    return the_names

def runTests(the_names):
    feature_sets = [(genderFeatures(n), g) for (n,g) in the_names]
    
    if False:
        train_set, test_set = feature_sets[500:], feature_sets[:500]
    else:
        train_set = apply_features(genderFeatures, the_names[500:])
        test_set  = apply_features(genderFeatures, the_names[:500])

    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print '-----------------------------'

    if True:
        def getGender(name):
            return classifier.classify(genderFeatures(name))
        def testClassifier(name):
           print name, 'is', getGender(name)

        test_names = ['Peter', 'Catherine', 'John', 'Madeline', 'Mark', 'Tom', 
                      'Matt', 'Matthew', 'David', 'Julie',
                      'Chris', 'Morgan', 'Riley']
        for name in test_names:
            testClassifier(name)
        print '-----------------------------'

    if False:
        for (n,g) in the_names[:500]:
            predicted = getGender(n)
            print '%10s is' % n, '%6s' % predicted, '(%6s)' % g, '***' if predicted != g else ''

    if False:
        def getDesc(a_list):
            return (len(a_list), sorted(a_list))
        print 'Correct (male) =', getDesc([n for (n,g) in the_names[:500] if getGender(n)==g and g =='male'])
        print '---------------------------------------------------'
        print 'Correct (female) =', getDesc([n for (n,g) in the_names[:500] if getGender(n)==g and g =='female'])
        print '===================================================='
        print 'Incorrect (male) =', getDesc([n for (n,g) in the_names[:500] if getGender(n)!=g and g =='male'])
        print '---------------------------------------------------'
        print 'Incorrect (female) =', getDesc([n for (n,g) in the_names[:500] if getGender(n)!=g and g =='female'])

    num_correct = len([1 for (n,g) in the_names[:500] if getGender(n)==g])
    total = len(the_names[:500])
    print num_correct, total
    accuracy = num_correct/total
    print 'accuracy = %.02f' % accuracy
    print 'accuracy = %.02f' % nltk.classify.accuracy(classifier, test_set)  

    classifier.show_most_informative_features(10)

def analyzeErrors(the_names):
    train_names = the_names[1500:]
    validation_names = the_names[500:1500]
    test_names = the_names[:500]

    train_set, validation_set, test_set = [apply_features(genderFeatures, n) 
                                           for n in [train_names, validation_names, test_names]]
    
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print 'validation accuracy = %.02f' % nltk.classify.accuracy(classifier, validation_set) 
    print '      test accuracy = %.02f' % nltk.classify.accuracy(classifier, test_set) 
    
    def getPrediction(name):
         return classifier.classify(genderFeatures(name))
    
    validation_results = [(n,g,getPrediction(n)) for (n,g) in validation_names]
    validation_results_incorrect = [(n,g,p) for (n,g,p) in validation_results if g!=p]
    validation_results_incorrect_male = [n for (n,g,p) in validation_results_incorrect if g=='male']
    validation_results_incorrect_female = [n for (n,g,p) in validation_results_incorrect if g=='female']
    print '--- %d males classified incorrectly ----------------------------------------' % len(validation_results_incorrect_male)
    print sorted(validation_results_incorrect_male)
    print '--- %d females classified incorrectly --------------------------------------' % len(validation_results_incorrect_female)
    print sorted(validation_results_incorrect_female)
    print len(validation_results_incorrect), 'incorrect in', len(validation_results)
    
    classifier.show_most_informative_features(20)

    def showPrediction(name):
        print name, 'is',  getPrediction(name)
        
        showPrediction('madeline')
   
train_names = the_names[1500:]
big_train_set = apply_features(genderFeatures, the_names) 
big_classifier = nltk.NaiveBayesClassifier.train(big_train_set) 
   
def predictGender(name, classify_only, dict_only):
    if not classify_only:
        if name.lower() in gender_dict.keys():
            return (gender_dict[name.lower()], 'dict')
    if not dict_only:
        return big_classifier.classify(genderFeatures(name)), 'classifier'
    return 'no match', 'none'
        
if __name__ == '__main__':
    print nltk.__doc__
    print '-----------------------------'
    the_names = getNames()
    print '%4d males'   % len([n for (n,g) in the_names if g == 'male'])
    print '%4d females' % len([n for (n,g) in the_names if g == 'female'])
    print '%4d total' % len(the_names)
    
    if False:
        runTests(the_names)
        
    if False:
        for i in range(1):
            the_names = getNames()
            
    if False:
        analyzeErrors(the_names)
    
    if True:
        print predictGender('Pierre')
            
