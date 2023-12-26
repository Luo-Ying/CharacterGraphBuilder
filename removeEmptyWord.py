import os
from pathlib import Path

code_of_special_character = [8212, 8217]

# unseless : C:conjunction, D:determiner, P:pronoun, I:interjection, F:punctuation
tag_of_usefull_word = ['N', 'R', 'V', 'Z', 'W'] # N:noun, R:adverb, V:verb, Z:number, W:date, 

# Remove the punctuations
def remove_punctuations(file_to_read, file_to_write):
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        with open(file_to_write+"_whithout_punctuation.txt", 'w', encoding='utf-8') as file_write:
            line = file_read.readline()
            while line:
                words = line.split()
                if words: 
                    if len(words[0]) > 1 and not ( ord(words[0][0]) < 65 or (ord(words[0][0]) > 90 and ord(words[0][0]) < 97) or (ord(words[0][0]) > 122 and ord(words[0][0]) < 192) or ord(words[0][0]) in code_of_special_character ):
                        file_write.write(line)
                line = file_read.readline()
                
                
def remove_uselessWords(file_to_write):
    
    with open(file_to_write+"_whithout_punctuation.txt", 'r', encoding='utf-8') as file_read:
        with open(file_to_write, 'w', encoding='utf-8') as file_write:
            line = file_read.readline()
            while line:
                words = line.split()
                if words: 
                    if len(words[2]) != "" and words[2][0] in tag_of_usefull_word:
                        file_write.write(line)
                line = file_read.readline()
                
    os.remove(file_to_write+"_whithout_punctuation.txt")
                
# Remove the usless words
def lemmatisation(file_to_read, file_to_write):
    remove_punctuations(file_to_read, file_to_write)
    remove_uselessWords(file_to_write)

def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# lemmatisation('test.txt')
def lemmatisationInCorpus():
    
    folder_freeling_result = "corpus/corpus_treated_by_Freeling/"
    folder_lemmatisation_result = "corpus/corpus_treated_lemmatisationFreeling/"
    
    checkAndCreateFoldert(folder_lemmatisation_result)
    
    path = Path(folder_freeling_result)
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        if os.path.exists(folder_lemmatisation_result + dir)==False: os.makedirs(folder_lemmatisation_result + dir)
        files = os.listdir(folder_freeling_result + dir)
        for file in files:
            file_to_read = folder_freeling_result + dir + "/" + file
            file_to_write = folder_lemmatisation_result + dir + "/" + file
            lemmatisation(file_to_read, file_to_write)
            
lemmatisationInCorpus()