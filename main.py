import numpy as np
import pickle
from data_classifier import extract_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import os

def train_small_set(size, path_to_corpus):
    centuries = ['1700', '1750', '1800', '1850', '1900', '1950', '2000']
    x_train = []
    y_train = []
    data_extraction = extract_data()
    
    for century in centuries:
        with open(f'{path_to_corpus}{century}.pk', 'rb') as file:
            new_corpus = pickle.load(file)
            data = new_corpus.get_data_point()[:size]
            x_train_temp, y_train_temp = data_extraction.get_machine_data(data, new_corpus.get_century())
            x_train = x_train + x_train_temp
            y_train = y_train + y_train_temp
    
    x_train_model = np.array(x_train)
    y_train_model = np.array(y_train)
    x_train, x_test, y_train, y_test = train_test_split(x_train_model, y_train_model, test_size = 0.15)
    
    # Random forest model
    classifier_tree = RandomForestClassifier()
    classifier_tree.fit(x_train, y_train)
    prediction_y = classifier_tree.predict(x_test)
    print('Random forest model: ')
    print(confusion_matrix(y_test, prediction_y))
    
    # Linear classifiers
    Linear = SGDClassifier(loss = 'log_loss')
    Linear.fit(x_train, y_train)
    prediction_y = Linear.predict(x_test)
    print('Linear using gradient descent: ')
    print(confusion_matrix(y_test, prediction_y))
    
def train_large_set(path_to_corpus, save_models):
    centuries = ['1700', '1750', '1800', '1850', '1900', '1950', '2000']
    x_train = []
    y_train = []
    data_extraction = extract_data()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Loading and processing corpuses')
    
    for century in centuries:
        with open(f'{path_to_corpus}{century}.pk', 'rb') as file:
            try:
                while True:
                    new_corpus = pickle.load(file)
                    data = new_corpus.get_data_point()
                    x_train_temp, y_train_temp = data_extraction.get_machine_data(data, new_corpus.get_century())
                    x_train = x_train + x_train_temp
                    y_train = y_train + y_train_temp
            except EOFError:
                pass
    print('Done loading corpuses, beginning training')
    x_train_model = np.array(x_train)
    y_train_model = np.array(y_train)
    x_train, x_test, y_train, y_test = train_test_split(x_train_model, y_train_model, test_size = 0.15)
    
    # Random forest model
    classifier_tree = RandomForestClassifier()
    classifier_tree.fit(x_train, y_train)
    with open(f'{save_models}Tree.pk', 'wb') as file:
        pickle.dump(classifier_tree, file)
    print('Random forest traning done')
    prediction_y = classifier_tree.predict(x_test)
    print('Random forest model: ')
    confusion = confusion_matrix(y_test, prediction_y)
    print(confusion)
    print(classification_report(y_test, prediction_y))
    
    # Linear classifiers
    Linear = SGDClassifier(loss = 'log_loss')
    Linear.fit(x_train, y_train)
    with open(f'{save_models}Linear.pk', 'wb') as file:
        pickle.dump(Linear, file)
    print('Linear traning done')
    prediction_y = Linear.predict(x_test)
    print('Linear using gradient descent: ')
    confusion = confusion_matrix(y_test, prediction_y)
    print(confusion)
    print(classification_report(y_test, prediction_y))
    
    # Neural network 100 lager
    Neural = MLPClassifier(hidden_layer_sizes = (100,), activation = 'logistic')
    Neural.fit(x_train, y_train)
    print('Neural classifier trained')
    prediction_y = Neural.predict(x_test)
    with open(f'{save_models}Neural.pk', 'wb') as file:
        pickle.dump(Neural, file)
    print('Neural network 100 layers, logistic function')
    confusion = confusion_matrix(y_test, prediction_y)
    print(confusion)
    print(classification_report(y_test, prediction_y))
    
    # Neural network 100 lager
    Neural = MLPClassifier(hidden_layer_sizes = (100,), activation = 'relu')
    Neural.fit(x_train, y_train)
    with open(f'{save_models}Neural.pk', 'wb') as file:
        pickle.dump(Neural, file)
    print('Neural classifier trained')
    prediction_y = Neural.predict(x_test)
    print('Neural network 1000 layers, relu function')
    confusion = confusion_matrix(y_test, prediction_y)
    print(confusion)
    print(classification_report(y_test, prediction_y))
    
def demo():
    centuries = ['1800', '2000']
    extracter = extract_data()
    os.system('cls' if os.name == 'nt' else 'clear')
    x_train = []
    y_train = []
    for century in centuries:
        with open(f'Test/{century}.pk', 'rb') as file:
            try:
                while True:
                    new_corpus = pickle.load(file)
                    data = new_corpus.get_data_point()
                    x_train_temp, y_train_temp = extracter.get_machine_data(data, new_corpus.get_century())
                    x_train = x_train + x_train_temp
                    y_train = y_train + y_train_temp
            except EOFError:
                pass
    x_test = np.array(x_train)
    y_test = np.array(y_train)
    print(y_test)
    with open('Models/Neural.pk', 'rb') as file:
        Neural = pickle.load(file)
    pred_y = Neural.predict(x_test)
    print(confusion_matrix(y_test, pred_y))
    print(classification_report(y_test, pred_y))
    
def demo2():
    os.system('cls' if os.name == 'nt' else 'clear')
    centuries = ['1700', '1750', '1800', '1850', '1900', '1950', '2000']
    extracter = extract_data()
    with open('Models_without_wordclasses/Neural.pk', 'rb') as file:
        Neural = pickle.load(file)
    while True:
        inputen = input('Skriv in en mening! \n')
        if inputen == 'exit':
            break
        prediction = Neural.predict([extracter.process_raw(inputen)])
        print(f'jag tror {centuries[prediction[0]]}')
    print('Ajdö')
    
        
        
    
#train_small_set(100)
save_models = 'Models/'
path_to_corpus = 'Korpusar_kortare/'
#train_large_set(path_to_corpus, save_models)
demo()
#demo2()