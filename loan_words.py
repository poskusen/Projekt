german = []
french = []
english = []


with open('loan_words/german.txt', 'r') as file:
    for line in file:
        german.append(line.strip('\n').strip().lower())
    
with open('loan_words/english.txt', 'r') as file:
    for line in file:
        english.append(line.strip('\n').strip().lower())

with open('loan_words/french.txt', 'r') as file:
    for line in file:
        french.append(line.strip('\n').strip().lower())
    
    



