import bz2
from data_point_class import data_point, century_corpus
import pickle
import sys
sys.stdout.reconfigure(encoding='utf-8')
word_classes_tracker = []
ILLEGAL = ['#', '*', '"', '.', ',', '?', '!', '-' , '`', '\'', '\n', '(', ')', ';', '/', ':', '»', '®', '', '--', '½', '', '§']
ILLEGAL = ILLEGAL + [str(i) for i in range(0,10)]
index = 0
index_to_words = {}
words_to_index = {}

def test_print(corpus_location, corpus_destination):
    with bz2.open(corpus_location, 'rt', encoding='utf-8') as file1:
        with open(f'{corpus_destination}.txt', 'w', encoding="utf-8") as file2:
            iter = 0
            for line in file1:
                file2.write(line)
                iter += 1
                if iter > 2000:
                    break
    

def process_corpus(corpus_location, corpus_destination, century, txt = True, amount_of_sentences = 10, corpus_type = 1):
    if corpus_type == 1:
        process_data_1(corpus_location, corpus_destination, century, txt, amount_of_sentences)
    elif corpus_type == 2:
        process_data_2(corpus_location, corpus_destination, century, txt, amount_of_sentences)

def process_data_1(corpus_location, corpus_destination, century, txt, amount_of_sentences):
    global word_classes_tracker
    global ILLEGAL
    Tot_len_sentence = 0
    tot_sentence = 0
    word_classes =  {}
    words = {}
    sentence_end = False
    if not txt:
        corpus = century_corpus(century)
    with bz2.open(corpus_location, 'rt', encoding='utf-8') as file: # Läser av korpus och konverterar till vårat format
        sentence_len = 0
        for line in file:
            if 'sentence' in line:
                if tot_sentence > amount_of_sentences and not txt:
                    if Tot_len_sentence != 0:
                        new_data_point = data_point(Tot_len_sentence/tot_sentence, words, word_classes)
                        corpus.add_data_point(new_data_point)
                    Tot_len_sentence = 0
                    tot_sentence = 0
                    word_classes =  {}
                    words = {}
                if sentence_end: # Avsluta meningen
                    Tot_len_sentence += sentence_len
                    tot_sentence += 1
                    sentence_len = 0
                    sentence_end = False 
                else: # Börja en ny mening
                    sentence_end = True 
            else:
                if sentence_end:
                    word = line.split('>')[1].replace('</w', '')
                    if word not in ILLEGAL:
                        if word.lower() in words:
                            words[word.lower()] += 1
                        else: 
                            words[word.lower()] = 1
                        word_class = line.split(' ')[1].replace('pos="', '')
                        word_class = word_class.replace('"', '')
                        if word_class in word_classes:
                            word_classes[word_class] += 1
                        else:
                            word_classes[word_class] = 1
                        sentence_len += 1
                        if word_class not in word_classes_tracker:
                            word_classes_tracker.append(word_class)
    if txt:
        with open(f'{corpus_destination}.txt', 'w', encoding="utf-8") as file:
            file.write(f'Corpus: {corpus_destination} \n')
            file.write(f'Average sentence length: {Tot_len_sentence/tot_sentence} \n')
            file.write(f'_______________________\n')
            file.write(f'Word class : amount in corpus\n')
            for word_class in word_classes:
                file.write(f'{word_class}: {word_classes[word_class]} \n')
            file.write(f'Word : amount in corpus\n')
            for word in words:
                file.write(f'{word} : {words[word]} \n')
            file.write(f'end of corpus -1')
    else:
        with open(f'{corpus_path}.pk', 'ab+') as file:
            pickle.dump(corpus, file)
                
                
def process_data_2(corpus_location, corpus_destination, century, txt, amount_of_sentences):
    global word_classes_tracker
    global ILLEGAL
    Tot_len_sentence = 0
    tot_sentence = 0
    word_classes =  {}
    words = {}
    sentence_end = False
    if not txt:
        corpus = century_corpus(century)
    with bz2.open(corpus_location, 'rt', encoding='utf-8') as file: # Läser av korpus och konverterar till vårat format
        sentence_len = 0
        for line in file:
            if 'sentence' in line:
                if tot_sentence > amount_of_sentences and not txt:
                    if Tot_len_sentence != 0:
                        new_data_point = data_point(Tot_len_sentence/tot_sentence, words, word_classes)
                        corpus.add_data_point(new_data_point)
                    Tot_len_sentence = 0
                    tot_sentence = 0
                    word_classes =  {}
                    words = {}
                if sentence_end: # Avsluta meningen
                    Tot_len_sentence += sentence_len
                    tot_sentence += 1
                    sentence_len = 0
                    sentence_end = False 
                else: # Börja en ny mening
                    sentence_end = True 
            elif 'token' in line:
                if sentence_end:
                    word = line.split('>')[1].replace('</token', '')
                    if word not in ILLEGAL:
                        if word.lower() in words:
                            words[word.lower()] += 1
                        else: 
                            words[word.lower()] = 1
                        holder = line.strip().split('pos="')[1]
                        word_class = holder[0] + holder[1]
                        if word_class in word_classes:
                            word_classes[word_class] += 1
                        else:
                            word_classes[word_class] = 1
                        if word_class not in word_classes_tracker:
                            word_classes_tracker.append(word_class)
                        sentence_len += 1

    if txt:
        with open(f'{corpus_destination}.txt', 'w', encoding="utf-8") as file:
            file.write(f'Corpus: {corpus_destination} \n')
            file.write(f'Average sentence length: {Tot_len_sentence/tot_sentence} \n')
            file.write(f'_______________________\n')
            file.write(f'Word class : amount in corpus\n')
            for word_class in word_classes:
                file.write(f'{word_class}: {word_classes[word_class]} \n')
            file.write(f'Word : amount in corpus\n')
            for word in words:
                file.write(f'{word} : {words[word]} \n')
            file.write(f'end of corpus -1')
    else:
        with open(f'{corpus_path}.pk', 'ab+') as file:
            pickle.dump(corpus, file)
type_1 = [('Korpusar_ej_extraherade/bloggmix2004.xml.bz2', 2000)
          ]
type_2 = [('Korpusar_ej_extraherade/kubhist2-lundsweckoblad-1810.xml.bz2', 1800), 
          ]
#corpus_path = f'Korpusar/test{century}_2'

# Type of corpus = (1, 2, 3, 4)
                            
for corpus in type_1:
    century = corpus[1]
    corpus_path = f'Test/{century}'
    process_corpus(corpus[0], corpus_path, century, txt = False, corpus_type=1)
    print(f'Done with: {corpus[0]}')

for corpus in type_2:
    century = corpus[1]
    corpus_path = f'Test/{century}'
    process_corpus(corpus[0], corpus_path, century, txt = False, corpus_type=2)
    print(f'Done with: {corpus[0]}')


# Open the .bz2 file
