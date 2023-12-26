import os

code_of_special_character = [8212, 8217]

# unseless : C:conjunction, D:determiner, P:pronoun, I:interjection, F:punctuation
tag_of_usefull_word = ['N', 'R', 'V', 'Z', 'W'] # N:noun, R:adverb, V:verb, Z:number, W:date, 

# Remove the punctuations
def remove_punctuations(modif_file):
    
    with open(modif_file, 'r', encoding='utf-8') as file_read:
        with open(modif_file+"_whithout_punctuation.txt", 'w', encoding='utf-8') as file_write:
            line = file_read.readline()
            while line:
                words = line.split()
                if words: 
                    if len(words[0]) > 1 and not ( ord(words[0][0]) < 65 or (ord(words[0][0]) > 90 and ord(words[0][0]) < 97) or (ord(words[0][0]) > 122 and ord(words[0][0]) < 192) or ord(words[0][0]) in code_of_special_character ):
                        file_write.write(line)
                line = file_read.readline()
    
    with open(modif_file, 'w') as file:
        file.write('')
                
def remove_uselessWords(modif_file):
    with open(modif_file+"_whithout_punctuation.txt", 'r', encoding='utf-8') as file_read:
        with open(modif_file, 'w', encoding='utf-8') as file_write:
            line = file_read.readline()
            while line:
                words = line.split()
                if words: 
                    if len(words[2]) != "" and words[2][0] in tag_of_usefull_word:
                        file_write.write(line)
                line = file_read.readline()
                
    os.remove(modif_file+"_whithout_punctuation.txt")
                
# Remove the usless words
def lemmatisation(input_filename):
    remove_punctuations(input_filename)
    remove_uselessWords(input_filename)

lemmatisation('test.txt')