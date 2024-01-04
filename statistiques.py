import os
from pathlib import Path
import string

# Nombre de mots par phrases, par chapitres, paragraphes
# Nombre de lettres par mots en moyenne
# Pourcentages de stopwords par chapitre
# Pourcentage de capitalized, uppercase, lowercase.
# Combien d'entités de NER détecter en moyenne par chapitre et dans le contexte de 25 mots. 最好获取均值, 中间值 和 标准差 ( 标准差： 反映一个数据集的离散程度 （或理解为数据集的波动大小）)
# Quelle est le pourcentage de Proper Noun dans les phrases.  均值， 中间值， 标准差



nbWordsOfChapter = 0
# nbWordsPerSentence = []
# nbCharactersOfParagraph = []
# nbUppercase = 0
# nbLowercase = 0
# nbCapitalized = 0
# nbStopWordsOfChpter = 0
# allEntityNameInAllContext = 0      # context = 25 mots
nbContext = 0

def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
        
def getNumberOfWordsPerSentence(file_to_read):
    
    nbWordsPerSentence = []
    
    nbWords = 0
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split()
            if words:
                for word in words:
                    if any(c in string.ascii_letters for c in word):
                        nbWords += 1
                        # if '’' in word and is_quote_surrounded_by_letters(word):
                        #     nbWords += 1
                    if ('.' in word or '!' in word or '?' in word) and nbWords != 0:
                        nbWordsPerSentence.append(nbWords)
                        nbWords = 0
            line = file_read.readline()
    return nbWordsPerSentence
    

def getNumberOfWordsInChapter(list_of_numbers_of_words_list):
    
    nbWordsOfChapter = 0
    
    for number in list_of_numbers_of_words_list:
        nbWordsOfChapter += number
        
    return nbWordsOfChapter


def is_quote_surrounded_by_letters(s):
    for i in range(1, len(s) - 1):
        if s[i] == "’" and s[i - 1].isalpha() and s[i + 1].isalpha():
            return True
    return False

def getNumberOfWordsPerParagraph(file_to_read):
    
    nbWordsOfParagraph = []
    
    nbWords = 0
    nbParagraph = 0
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            if len(line) > 4 and f"{line[0]}{line[1]}{line[2]}{line[3]}" == "    ":
                nbParagraph += 1
                if nbWords != 0:
                    nbWordsOfParagraph.append(nbWords)
                nbWords = 0
            words = line.split()
            for word in words:
                if any(c in string.ascii_letters for c in word):
                    nbWords += 1
                    # if '’' in word and is_quote_surrounded_by_letters(word):
                    #     nbWords += 1
            line = file_read.readline()
    return nbWordsOfParagraph



def getAllCharactersInChapiter(file_to_read):
    
    countAllCharacters = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            for char in line:
                if char.isalpha():
                    countAllCharacters += 1
            line = file_read.readline()
            
    return countAllCharacters



def getNumberOfUppercase(file_to_read):
    
    countUppercase = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            for char in line:
                if char.isupper():
                    countUppercase += 1
            line = file_read.readline()
                    
    return countUppercase

def getNumberOfCapitalized(file_to_read):
    
    countCapitalized = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split()
            for word in words:
                if word.istitle():
                    countCapitalized += 1
            line = file_read.readline()
                    
    return countCapitalized


def getNumberOfStopWords(file_to_read):
    
    countStopWords = 0
    
    # unseless : C:conjunction, D:determiner, P:pronoun, I:interjection, F:punctuation
    tag_of_usefull_word = ['N', 'R', 'V', 'Z', 'W'] # N:noun, R:adverb, V:verb, Z:number, W:date, 
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split()
            if words:
                if words[2] != "" and words[2][0] not in tag_of_usefull_word:
                    countStopWords += 1
            line = file_read.readline()
    
    return countStopWords


# TODO: Enlever aussi les tops words 
def getNumberOfEntityNameInEachContext(file_to_read_context, file_to_read_EntityName):
    
    entityName_list = []
    
    nbEntityNameInEachContext = []
    
    # Get entity name list
    with open(file_to_read_EntityName, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split()
            if words:
                if words[0] != "": # and words[0] not in stopwords
                    entityName_list.append(words[0])
            line = file_read.readline()
    
    with open(file_to_read_context, 'r', encoding='utf-8') as file_read:
        countEntityName = 0
        line = file_read.readline()
        while line:
            words = line.split()
            if words:
                for word in words:
                    if word in entityName_list:
                        countEntityName += 1
            nbEntityNameInEachContext.append(countEntityName)
            countEntityName = 0
            line = file_read.readline()
            
    return nbEntityNameInEachContext
            

def getMinValueInList(lst):
    
    sorted_lst = sorted(lst)
    min_val = sorted_lst[0]
    
    return min_val

def getMaxValueInList(lst):
    
    sorted_lst = sorted(lst)
    max_val = sorted_lst[-1]
    
    return max_val

def getMedianValueInList(lst):
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

    return int(median)

def getAverageValueInList(lst):
    
    total = sum(lst)
    average = total / len(lst)
    return int(average)

def statistiques():
    
    folder_statistiques = "corpus/corpus_statistiques/"
    
    folder_source = "corpus/corpus_asimov_leaderboard/"
    
    folder_Freeling = "corpus/corpus_treated_by_Freeling/"
    folder_tokens = "corpus/corpus_tokens/"
    folder_entityName = "corpus/corpus_treated_merge_of_Freeling&Spacy/"
    
    checkAndCreateFoldert(folder_statistiques)
    
    path = Path(folder_tokens)
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        if os.path.exists(folder_statistiques + dir)==False: os.makedirs(folder_statistiques + dir)
        files = os.listdir(folder_tokens + dir)
        for file in files:
            
            file_to_write = folder_statistiques + dir + "/" + file
            
            with open(file_to_write, 'w', encoding='utf-8') as file_write:
                file_to_read_source = folder_source + dir + "/" + file + ".preprocessed"
                file_to_read_Freeling = folder_Freeling + dir + "/" + file
                file_to_read_tokens = folder_tokens + dir + "/" + file
                file_to_read_entityName = folder_entityName + dir + "/" + file
        
                # Nombre de mots par phrase
                nbWordsPerSentence = getNumberOfWordsPerSentence(file_to_read_source)
                # Nombre de mots par paragraphe
                nbWordsPerParagraph = getNumberOfWordsPerParagraph(file_to_read_source)   
                # Nombre de mots dans le chapitre
                nbWordsOfChapter = getNumberOfWordsInChapter(nbWordsPerSentence)
                nbUppercase = getNumberOfUppercase(file_to_read_source)
                nbLowercase = getAllCharactersInChapiter(file_to_read_source) - nbUppercase
                nbCapitalized = getNumberOfCapitalized(file_to_read_source)
                
                
                nbStopWordsOfChpter = getNumberOfStopWords(file_to_read_Freeling)
                nbEntityNameInEachContext = getNumberOfEntityNameInEachContext(file_to_read_tokens, file_to_read_entityName)
                
                min_nbWordsPerSentence = getMinValueInList(nbWordsPerSentence)
                max_nbWordsPerSentence = getMaxValueInList(nbWordsPerSentence)
                median_nbWordsPerSentence = getMedianValueInList(nbWordsPerSentence)
                average_nbWordsPerSentence = getAverageValueInList(nbWordsPerSentence)
                
                min_nbWordsPerParagraph = getMinValueInList(nbWordsPerParagraph)
                max_nbWordsPerParagraph = getMaxValueInList(nbWordsPerParagraph)
                median_nbWordsPerParagraph = getMedianValueInList(nbWordsPerParagraph)
                average_nbWordsPerParagraph = getAverageValueInList(nbWordsPerParagraph)
                
                min_nbEntityNameInEachContext = getMinValueInList(nbEntityNameInEachContext)
                max_nbEntityNameInEachContext = getMaxValueInList(nbEntityNameInEachContext)
                median_nbEntityNameInEachContext = getMedianValueInList(nbEntityNameInEachContext)
                average_nbEntityNameInEachContext = getAverageValueInList(nbEntityNameInEachContext)
                
                file_write.write("Nombre de mots par phrase\n" + str(nbWordsPerSentence) + "\n")
                file_write.write("Min:" + str(min_nbWordsPerSentence) + "\n")
                file_write.write("Max:" + str(max_nbWordsPerSentence) + "\n")
                file_write.write("Median:" + str(median_nbWordsPerSentence) + "\n")
                file_write.write("Average:" + str(average_nbWordsPerSentence) + "\n\n")
                
                file_write.write("Nombre de mots par paragraph\n" + str(nbWordsPerParagraph) + "\n")
                file_write.write("Min:" + str(min_nbWordsPerParagraph) + "\n")
                file_write.write("Max:" + str(max_nbWordsPerParagraph) + "\n")
                file_write.write("Median:" + str(median_nbWordsPerParagraph) + "\n")
                file_write.write("Average:" + str(average_nbWordsPerParagraph) + "\n\n")
                
                
                file_write.write("Nombre de mots totale dans le chapitre\n" + str(nbWordsOfChapter) + "\n\n")
                
                file_write.write("Nombre d'uppercase\n" + str(nbUppercase) + "\n\n")
                
                file_write.write("Nombre de lowercase\n" + str(nbLowercase) + "\n\n")
                
                file_write.write("Nombre de capitalized\n" + str(nbCapitalized) + "\n\n")
                
                file_write.write("Nombre de stopwords\n" + str(nbStopWordsOfChpter) + "\n\n")
                
                file_write.write("Nombre d'EntityName dans chaque context\n" + str(nbEntityNameInEachContext) + "\n")
                file_write.write("Min:" + str(min_nbEntityNameInEachContext) + "\n")
                file_write.write("Max:" + str(max_nbEntityNameInEachContext) + "\n")
                file_write.write("Median:" + str(median_nbEntityNameInEachContext) + "\n")
                file_write.write("Average:" + str(average_nbEntityNameInEachContext) + "\n\n")
                
                file_write.write("Nombre de context totale dans le chapitre\n" + str(len(nbEntityNameInEachContext)) + "\n\n")

                # print("Nombre de mots par phrase" + str(nbWordsPerSentence))
                # print("Nombre de mots par paragraph" + str(nbWordsPerParagraph))
                # print("Nombre de mots par chapitre: " + str(nbWordsOfChapter))
                # print("nombre uppercase: " + str(nbUppercase))
                # print("nombre lowercase: " + str(nbLowercase))
                # print("nombre capitalized: " + str(nbCapitalized))
                # print("nombre stopwords: " + str(nbStopWordsOfChpter))
                # print("nombre entity name dans chaque context: " + str(nbEntityNameInEachContext))
                # print("nombre de context: " + str(len(nbEntityNameInEachContext)))

statistiques()