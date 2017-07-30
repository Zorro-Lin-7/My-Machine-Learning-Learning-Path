import random
from nltk.corpus import names
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy

# To define a function to extract features from input words
# 名字的最后几个字母作为特征
def gender_features(word, num_letters=2): 
    return {'feature': word[-num_letters:].lower()}
    
if __name__ == '__main__':
    # training data:
    labeled_names = ([(name, 'male') for name in names.words('male.txt')]
                    + [(name, 'female') for name in names.words('female.txt')])
    random.seed(7)
    random.shuffle(labeled_names) 
    
    # test data:
    input_names = ['Leonardo', 'Amy', 'Sam']
    
    # 因为我们不知道该截取的词尾长度，所以我们将遍历parameter space from 1 to 5，看看用哪个的准确度最高
    for i in range(1, 5):
        print("\nNumber of letters:", i)
        feature_sets = [(gender_features(n, i), gender) for (n, gender) in labeled_names]
        train_set, test_set = feature_sets[500:], feature_sets[:500]
        classifier = NaiveBayesClassifier.train(train_set)
        print("Accuracy ==>", str(100 * nltk_accuracy(classifier, test_set)) +str('%'))
        
        # Predict
        for name in input_names:
            print(name, "==>", classifier.classify(gender_features(name, i)))