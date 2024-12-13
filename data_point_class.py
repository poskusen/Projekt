class century_corpus():
    def __init__(self, century):
        self.century = century
        self.data_points = []
        self.taken = 0
        
    def get_century(self):
        return self.century
    
    def get_data_point(self):
        return self.data_points
    
    def add_data_point(self, point):
        self.data_points.append(point)
    def get_next_point(self):
        data = self.data_points[self.taken]
        self.taken += 1
        return data
        
    def __str__(self):
        return f'Century: {self.century} \n Datapoints: {len(self.data_points)}'
    
class data_point:
    def __init__(self, avg_sentence_len, words, word_classes = None):
        self.avg_sentence_len = avg_sentence_len
        self.words = words
        self.word_classes = word_classes
    
    def get_words(self):
        return self.words
    
    def get_word_classes(self):
        return self.word_classes
    
    def get_avg_sen(self):
        return self.avg_sentence_len
    
    def __str__(self):
        string = f'Sentence length: {self.avg_sentence_len} \n'
        for word in self.words:
            string = string + f'{word} : {self.words[word]} \n'
        for word_class in self.word_classes:
            string = string + f'{word_class} : {self.word_classes[word_class]} \n'
        return string
    