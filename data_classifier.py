from data_point_class import data_point
from loan_words import french
from loan_words import german
from loan_words import english
import numpy as np

import pickle

class extract_data():
    '''Converts data_points to training material'''
    def __init__(self):
        self.words = {}
    
    def get_machine_data(self, data_list, label):
        data_points = []
        data_label = []
        for data in data_list:
            new_format, new_label = self.convert_point(data, label)
            data_points.append(new_format)
            data_label.append(new_label)
        return data_points, data_label
        
            
    def convert_point(self, data, label):
        centuries = [1700, 1750, 1800, 1850, 1900, 1950, 2000]
        centuries_in_number = centuries.index(label)
        new_format = []
        new_format.append(self.get_sentence_length(data))
        new_format = new_format + self.get_amount_loan_words(data)
        new_format = new_format + self.old_words(data)
        new_format = new_format + self.wordtype(data)
        return new_format, centuries_in_number
        
            
    def get_sentence_length(self, data):
        return data.get_avg_sen()
    
    def get_amount_loan_words(self, data):
        german_words = 0
        french_words = 0
        english_words = 0
        words_in_data = data.get_words()
        for word in german:
            if word in words_in_data.keys():
                german_words += words_in_data[word]
        for word in french:
            if word in words_in_data.keys():
                french_words += words_in_data[word]
        for word in english:
            if word in words_in_data.keys():
                english_words += words_in_data[word]
        return [german_words, french_words, english_words]
    
        
    def wordtype(self, data):
        word_classes = ['NN', 'PP', 'PM', 'RG', 'JJ', 'VB', 'KN', 'PC', 'HA', 'PN', 'DT', 'AB', 'HP', 'PS', 'SN', 'PL', 'IE', 'RO', 'UO', 'IN', 'HD', 'HS', 'PAD', 'MAD', 'MID', 'PA', 'NL']
        new_format = [0 for _ in word_classes]
        for word_class in data.get_word_classes():
            if word_class == 'MI':
                word_class_holder = 'MID'
            elif word_class == 'MA':
                word_class_holder = 'MAD'
            else:
                word_class_holder = word_class
            new_format[word_classes.index(word_class_holder)] = data.get_word_classes()[word_class]
        return new_format
    
    def old_words(self, data):
        words_in_data = data.get_words()
        old_pre = ['qv', 'dt', 'hv', 'fv', 'dh']
        new_format = [0 for _ in old_pre]
        for word in words_in_data:
            for i in range(len(old_pre) - 1):
                if old_pre[i] in word:
                    new_format[i] += 1
        return new_format
    
    def process_raw(self, data):
        words = {}
        amount_of_sentences = data.count('.') + 1
        amount_of_words = data.count(' ') + data.count('.') + 1
        word_list = data.replace('.', '').replace(',', '').split(' ')
       
                
        for word in word_list:
            if word in words:
                words[word.lower()] += 1
            else: 
                words[word.lower()] = 1
        data = data_point(amount_of_words/amount_of_sentences, words)
        new_format = [self.get_sentence_length(data)]
        new_format = new_format + self.get_amount_loan_words(data)
        new_format = new_format + self.old_words(data)
        #new_format = new_format + self.wordtype(data)
        return new_format
                    
            
        
        
        
        
        
        

    
            
        
    