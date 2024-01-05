import os
from pathlib import Path

def buildTokens(file_to_read, file_to_write):
   
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        lines = file_read.readlines()
        
    with open(file_to_write, 'w', encoding='utf-8') as file_write:
        for i in range(len(lines)):
            content = ''
            chunk = lines[i:i+60]
            if len(chunk) < 60:
                break
            for line in chunk:
                words = line.split()
                if words and words[0] != '':
                    content += words[0] + ' '
            content += '\n'
            file_write.write(content)

def checkAndCreateFoldert(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def buildTokensInFiles():
    
    folder_lemmatisation = "corpus/corpus_treated_lemmatisationFreeling/"
    folder_tokens = "corpus/corpus_tokens/"
    
    checkAndCreateFoldert(folder_tokens)
    
    path = Path(folder_lemmatisation)
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        if os.path.exists(folder_tokens + dir)==False: os.makedirs(folder_tokens + dir)
        files = os.listdir(folder_lemmatisation + dir)
        for file in files:
            file_to_read = folder_lemmatisation + dir + "/" + file
            file_to_write = folder_tokens + dir + "/" + file
            buildTokens(file_to_read, file_to_write)
