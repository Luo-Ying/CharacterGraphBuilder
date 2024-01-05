import os
from pathlib import Path
import string
import json

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
            words = line.split(' ')
            for word in words:
                countAllCharacters += 1
            line = file_read.readline()
            
    return countAllCharacters



def getNumberOfUppercase(file_to_read):
    
    countUppercase = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split(' ')
            for word in words:
                if word.isupper():
                    countUppercase += 1
            line = file_read.readline()
                    
    return countUppercase

def getNumberOfLowercase(file_to_read):
    
    countLowercase = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split(' ')
            for word in words:
                if word.islower():
                    countLowercase += 1
            line = file_read.readline()
                    
    return countLowercase

def getNumberOfOther(file_to_read):
    
    countOther = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split(' ')
            for word in words:
                if word.islower()==False and  word.isupper()==False and  word.istitle()==False:
                    countOther += 1
            line = file_read.readline()
                    
    return countOther

def getNumberOfCapitalized(file_to_read):
    
    countCapitalized = 0
    
    with open(file_to_read, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split(' ')
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
    
    with open('stopWords', 'r', encoding='utf-8') as file:
        stopWords = [line.strip() for line in file]
    
    # Get entity name list
    with open(file_to_read_EntityName, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            words = line.split()
            if words:
                if words[0] != "" and words[0] not in stopWords: # and words[0] not in stopwords
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
    # return "{:.1f}".format(round(average, 1)) 
    return round(average, 1)


def json_serialize_with_inline_arrays(obj, indent=4):
    if isinstance(obj, list):
        return json.dumps(obj, ensure_ascii=False)
    elif isinstance(obj, dict):
        items = []
        for key, value in obj.items():
            serialized_value = json_serialize_with_inline_arrays(value, indent)
            items.append(f'{" " * indent}"{key}": {serialized_value}')
        return "{\n" + ",\n".join(items) + "\n}"
    else:
        return json.dumps(obj, ensure_ascii=False)


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
            
            file_to_write = folder_statistiques + dir + "/" + file + ".json"
            
            # with open(file_to_write, 'w', encoding='utf-8') as file_write:
            file_to_read_source = folder_source + dir + "/" + file + ".preprocessed"
            file_to_read_Freeling = folder_Freeling + dir + "/" + file
            file_to_read_tokens = folder_tokens + dir + "/" + file
            file_to_read_entityName = folder_entityName + dir + "/" + file
    
            # Nombre de mots par phrase
            nbWordsPerSentence = getNumberOfWordsPerSentence(file_to_read_source)
            # Nombre de mots par paragraphe
            nbWordsPerParagraph = getNumberOfWordsPerParagraph(file_to_read_source)   
            # Nombre de mots dans le chapitre
            nbWordsOfChapter = getAllCharactersInChapiter(file_to_read_source)
            nbUppercase = getNumberOfUppercase(file_to_read_source)
            nbLowercase = getNumberOfLowercase(file_to_read_source)
            nbCapitalized = getNumberOfCapitalized(file_to_read_source)
            nbOther = getNumberOfOther(file_to_read_source)
            
            
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
            
            data = {
                "words_in_phrase":{
                    "data": nbWordsPerSentence,
                    "min": min_nbWordsPerSentence,
                    "max": max_nbWordsPerSentence,
                    "median": median_nbWordsPerSentence,
                    "average": average_nbWordsPerSentence
                },
                "words_in_paragraph":{
                    "data": nbWordsPerParagraph,
                    "min": min_nbWordsPerParagraph,
                    "max": max_nbWordsPerParagraph,
                    "median": median_nbWordsPerParagraph,
                    "average": average_nbWordsPerParagraph
                },
                "words_in_chapter": nbWordsOfChapter,
                "uppercase": nbUppercase,
                "lowercase": nbLowercase,
                "capitalized": nbCapitalized,
                "other": nbOther,
                "stop_words": nbStopWordsOfChpter,
                "entityName_in_context": {
                    "data": nbEntityNameInEachContext,
                    "min": min_nbEntityNameInEachContext,
                    "max": max_nbEntityNameInEachContext,
                    "median": median_nbEntityNameInEachContext,
                    "average": average_nbEntityNameInEachContext
                },
                "context_in-chapter": nbEntityNameInEachContext
            }
            
            formatted_json = json_serialize_with_inline_arrays(data)
            
            with open(file_to_write, 'w', encoding='utf-8') as file_write:
                file_write.write(formatted_json)
                
                # file_write.write("{")
                
                # file_write.write('"mots_par_phrase": {')
                # file_write.write('"data":' + str(nbWordsPerSentence) + ",")
                # file_write.write('"Min":' + str(min_nbWordsPerSentence) + ",")
                # file_write.write('"Max":' + str(max_nbWordsPerSentence) + ",")
                # file_write.write('"Median":' + str(median_nbWordsPerSentence) + ",")
                # file_write.write('"Average":' + str(average_nbWordsPerSentence) + "},")
                
                # file_write.write("mots_par_paragraph:" + str(nbWordsPerParagraph) + "\n")
                # file_write.write("Min:" + str(min_nbWordsPerParagraph) + "\n")
                # file_write.write("Max:" + str(max_nbWordsPerParagraph) + "\n")
                # file_write.write("Median:" + str(median_nbWordsPerParagraph) + "\n")
                # file_write.write("Average:" + str(average_nbWordsPerParagraph) + "\n\n")
                
                # file_write.write("Nombre de mots totale dans le chapitre\n" + str(nbWordsOfChapter) + "\n\n")
                
                # file_write.write("Nombre d'uppercase\n" + str(nbUppercase) + "\n\n")
                
                # file_write.write("Nombre de lowercase\n" + str(nbLowercase) + "\n\n")
                
                # file_write.write("Nombre de capitalized\n" + str(nbCapitalized) + "\n\n")
                
                # file_write.write("Nombre de other\n" + str(nbOther) + "\n\n")
                
                # file_write.write("Nombre de stopwords\n" + str(nbStopWordsOfChpter) + "\n\n")
                
                
                # file_write.write("entityname_par_context:" + str(nbEntityNameInEachContext) + "\n")
                # file_write.write("Min:" + str(min_nbEntityNameInEachContext) + "\n")
                # file_write.write("Max:" + str(max_nbEntityNameInEachContext) + "\n")
                # file_write.write("Median:" + str(median_nbEntityNameInEachContext) + "\n")
                # file_write.write("Average:" + str(average_nbEntityNameInEachContext) + "\n\n")
                
                # file_write.write("Nombre de context totale dans le chapitre\n" + str(len(nbEntityNameInEachContext)) + "\n\n")

                # file_write.write("}")
statistiques()

