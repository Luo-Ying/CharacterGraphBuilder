import os
from pathlib import Path
import string
import json
import re

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


def getEntityNameList(file_to_read_EntityName):
    entityName_list = []
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
    return entityName_list


def getNumberOfEntityNameInEachContext(file_to_read_context, file_to_read_EntityName):
    
    entityName_list = getEntityNameList(file_to_read_EntityName)
    
    nbEntityNameInEachContext = []
    
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


def modifyLine(line, entityname_list):
    for entityname in entityname_list:
        if '_' in entityname:
            new_entity = entityname.replace('_', ' ')
            line = line.replace(new_entity, entityname)
    return line

def remove_punctuation_if_right_empty(text):
    pattern = re.compile(r'([^\w\s])\s')
    matches = re.finditer(pattern, text)

    for match in matches:
        punctuation = match.group(1)
        text = text.replace(match.group(0), punctuation)

    return text

def getNumberOfWordsBetweenEachEntityname(file_to_read_source, file_to_read_EntityName):
    
    entityName_list = getEntityNameList(file_to_read_EntityName)
    
    nbWordsBetweenEachEntityname = []
    
    with open(file_to_read_source, 'r', encoding='utf-8') as file_read:
        countWords = 0
        isStart = False
        line = file_read.readline()
        while line:
            line = modifyLine(line, entityname_list=entityName_list)
            arr = []
            words = line.split(' ')
            if words:
                for word in words:
                    word = remove_punctuation_if_right_empty(word)
                    if word == ' ' or len(word)<=0:
                        continue
                    # print(word)
                    isContain = False
                    for entityname in entityName_list:
                        if len(word) <= 3 and word == entityname:
                            isContain = True
                        elif len(word) > 3 and word in entityname:
                            isContain = True
                    if isContain and not isStart:
                        isStart = True
                        countWords = 0
                        arr.append((word,'PER'))
                    elif isContain and isStart:
                        nbWordsBetweenEachEntityname.append(countWords)
                        countWords = 0
                        arr.append((word,'PER'))
                    else :
                        countWords += 1
                        arr.append((word,'O'))
            line = file_read.readline()
    return nbWordsBetweenEachEntityname
                    

def getCountNP(file_to_read):
    
    f_in = open(file_to_read, "r", encoding="utf-8")
    content = f_in.read()
    f_in.close()

    content = [c.split(" ")[2] for c in content.split("\n") if len(c) > 0]
    are_np = [c.startswith("NP") for c in content]

    return sum(are_np)

def getPercentNP(file_to_read):
    
    f_in = open(file_to_read, "r", encoding="utf-8")
    content = f_in.read()
    f_in.close()

    content = [c.split(" ")[2] for c in content.split("\n") if len(c) > 0]
    are_np = [c.startswith("NP") for c in content]

    percentNP = round(sum(are_np) / len(are_np), 2)
    return percentNP

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
    
    folder_source_pretread = "corpus/corpus_reformed/"
    
    folder_Freeling = "corpus/corpus_treated_by_Freeling/"
    folder_tokens = "corpus/corpus_tokens/"
    folder_entityName = "corpus/corpus_treated_merge_of_Freeling&Spacy/"
    
    checkAndCreateFoldert(folder_statistiques)
    
    path = Path(folder_tokens)
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        
        nbChapter = 0
        
        nbEntityNamePerChapter = []
        
        nbTimesDistance = 0
        sumDistanceTotale = 0
        sumOfMedianDistance = 0
        
        sumAverageWordsOfPhrase = 0
        sumAverageWordsOfParagraph = 0
        
        sumWordsInChapter = 0
        sumUppercase = 0
        sumLowercase = 0
        sumCapitalized = 0
        sumOther = 0
        
        sumStopWords = 0
        sumProperNoun = 0
        sumEntityname = 0
        
        sumEntitynameInContextAverage = 0
        
        if os.path.exists(folder_statistiques + dir)==False: os.makedirs(folder_statistiques + dir)
        files = os.listdir(folder_tokens + dir)
        for file in files:
            
            nbChapter += 1
            
            file_to_write = folder_statistiques + dir + "/" + file + ".json"
            
            # with open(file_to_write, 'w', encoding='utf-8') as file_write:
            file_to_read_source = folder_source + dir + "/" + file + ".preprocessed"
            file_to_read_source_pretread = folder_source_pretread + dir + "/" + file
            file_to_read_Freeling = folder_Freeling + dir + "/" + file
            file_to_read_tokens = folder_tokens + dir + "/" + file
            file_to_read_entityName = folder_entityName + dir + "/" + file
    
            # Nombre de mots par phrase
            nbWordsPerSentence = getNumberOfWordsPerSentence(file_to_read_source)
            # Nombre de mots par paragraphe
            nbWordsPerParagraph = getNumberOfWordsPerParagraph(file_to_read_source)   
            # Nombre de mots dans le chapitre
            nbWordsOfChapter = getAllCharactersInChapiter(file_to_read_source)
            
            sumWordsInChapter += nbWordsOfChapter
            
            nbUppercase = getNumberOfUppercase(file_to_read_source)
            uppercasePercent = round(nbUppercase/nbWordsOfChapter, 2)
            
            sumUppercase += (uppercasePercent * 100)
            
            nbLowercase = getNumberOfLowercase(file_to_read_source)
            lowercasePercent = round(nbLowercase/nbWordsOfChapter, 2)
            
            sumLowercase += (lowercasePercent * 100)
            
            nbCapitalized = getNumberOfCapitalized(file_to_read_source)
            capitalizedPercent = round(nbCapitalized/nbWordsOfChapter, 2)
            
            sumCapitalized += (capitalizedPercent * 100)
            
            nbOther = getNumberOfOther(file_to_read_source)
            otherPercent = round(nbOther/nbWordsOfChapter, 2)
            
            sumOther += (otherPercent * 100)
            
            
            nbStopWordsOfChpter = getNumberOfStopWords(file_to_read_Freeling)
            stopWordsPercent = round(nbStopWordsOfChpter/nbWordsOfChapter, 2)
            
            sumStopWords += (stopWordsPercent * 100)
            
            properNoun = getCountNP(file_to_read_Freeling)
            properNounPercent = getPercentNP(file_to_read_Freeling) * 100
            sumProperNoun += properNounPercent
            
            nbEntityNameInChapiter = len(getEntityNameList(file_to_read_entityName))
            entitynamePercent = round(nbEntityNameInChapiter/nbWordsOfChapter, 2) * 100
            sumEntityname += entitynamePercent
            
            nbEntityNamePerChapter.append(nbEntityNameInChapiter)
            nbEntityNameInEachContext = getNumberOfEntityNameInEachContext(file_to_read_tokens, file_to_read_entityName)
            nbWordsBetweenEntityname = getNumberOfWordsBetweenEachEntityname(file_to_read_source_pretread, file_to_read_entityName)
            print(len(nbWordsBetweenEntityname))
            nbTimesDistance += len(nbWordsBetweenEntityname)
            sumDistanceTotale += sum(nbWordsBetweenEntityname)
            
            
            min_nbWordsPerSentence = getMinValueInList(nbWordsPerSentence)
            max_nbWordsPerSentence = getMaxValueInList(nbWordsPerSentence)
            median_nbWordsPerSentence = getMedianValueInList(nbWordsPerSentence)
            average_nbWordsPerSentence = getAverageValueInList(nbWordsPerSentence)
            sumAverageWordsOfPhrase += average_nbWordsPerSentence
            
            min_nbWordsPerParagraph = getMinValueInList(nbWordsPerParagraph)
            max_nbWordsPerParagraph = getMaxValueInList(nbWordsPerParagraph)
            median_nbWordsPerParagraph = getMedianValueInList(nbWordsPerParagraph)
            average_nbWordsPerParagraph = getAverageValueInList(nbWordsPerParagraph)
            sumAverageWordsOfParagraph += average_nbWordsPerParagraph
            
            
            min_nbEntityNameInEachContext = getMinValueInList(nbEntityNameInEachContext)
            max_nbEntityNameInEachContext = getMaxValueInList(nbEntityNameInEachContext)
            median_nbEntityNameInEachContext = getMedianValueInList(nbEntityNameInEachContext)
            average_nbEntityNameInEachContext = getAverageValueInList(nbEntityNameInEachContext)
            
            sumEntitynameInContextAverage += average_nbEntityNameInEachContext
            
            min_nbWordsBetweenEntityname = getMinValueInList(nbWordsBetweenEntityname)
            max_nbWordsBetweenEntityname = getMaxValueInList(nbWordsBetweenEntityname)
            median_nbWordsBetweenEntityname = getMedianValueInList(nbWordsBetweenEntityname)
            average_nbWordsBetweenEntityname = getAverageValueInList(nbWordsBetweenEntityname)
            
            sumOfMedianDistance += median_nbWordsBetweenEntityname
            
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
                "uppercase_%": uppercasePercent * 100,
                "lowercase": nbLowercase,
                "lowercase_%": lowercasePercent * 100,
                "capitalized": nbCapitalized,
                "capitalized_%": capitalizedPercent * 100,
                "other": nbOther,
                "other_%": otherPercent * 100,
                "stop_words": nbStopWordsOfChpter,
                "stop_words_%": stopWordsPercent * 100,
                "proper_noun": properNoun,
                "proper_noun_%": properNounPercent,
                "entityName_in_chapiter": nbEntityNameInChapiter,
                "entityname_%": entitynamePercent,
                "entityName_in_context": {
                    "data": nbEntityNameInEachContext,
                    "min": min_nbEntityNameInEachContext,
                    "max": max_nbEntityNameInEachContext,
                    "median": median_nbEntityNameInEachContext,
                    "average": average_nbEntityNameInEachContext
                },
                "words_between_entityname": {
                    "data": nbWordsBetweenEntityname,
                    "min": min_nbWordsBetweenEntityname,
                    "max": max_nbWordsBetweenEntityname,
                    "median": median_nbWordsBetweenEntityname,
                    "average": average_nbWordsBetweenEntityname
                },
                "context_in_chapter": len(nbEntityNameInEachContext)
            }
            
            formatted_json = json_serialize_with_inline_arrays(data)
            
            with open(file_to_write, 'w', encoding='utf-8') as file_write:
                file_write.write(formatted_json)
                
        file_to_write_stat_of_book = folder_statistiques + dir + "/statistique_of_book.json"
        
        min_stat_entityname_in_book = getMinValueInList(nbEntityNamePerChapter)
        max_stat_entityname_in_book = getMaxValueInList(nbEntityNamePerChapter)
        median_stat_entityname_in_book = getMedianValueInList(nbEntityNamePerChapter)
        average_stat_entityname_in_book = getAverageValueInList(nbEntityNamePerChapter)
        
        
        
        data_stat_book = {
            "phrase_in_chapter_average_words": round(sumAverageWordsOfPhrase/nbChapter, 2),
            "paragraph_in_chapter_average_words": round(sumAverageWordsOfParagraph/nbChapter, 2),
            "chapter_average_words": round(sumWordsInChapter/nbChapter, 2),
            "uppercase_book_%": round(sumUppercase/nbChapter, 2),
            "lowercase_book_%": round(sumLowercase/nbChapter, 2),
            "capitalized_book_%": round(sumCapitalized/nbChapter, 2),
            "other_book_%": round(sumOther/nbChapter, 2),
            "stop_words_%": round(sumStopWords/nbChapter, 2),
            "proper_noun_%": round(sumProperNoun/nbChapter, 2),
            "entityname_%": round(sumEntityname/nbChapter, 2),
            "entityname_book": {
                "data": nbEntityNamePerChapter,
                "min_entity_per_chapter": min_stat_entityname_in_book,
                "max_entity_per_chapter": max_stat_entityname_in_book,
                "median_entity_per_chapter": median_stat_entityname_in_book,
                "average_entity_per_chapter": average_stat_entityname_in_book
                },
            "entityname_context_average": round(sumEntitynameInContextAverage/nbChapter, 2),
            "average_distance_between_entityname": round(sumDistanceTotale/nbTimesDistance, 2),
            "median_distance_beetween_entityname": round(sumOfMedianDistance/nbChapter, 2)
            
        }
        formatted_json_stat_book = json_serialize_with_inline_arrays(data_stat_book)
        with open(file_to_write_stat_of_book, 'w', encoding='utf-8') as file_write:
            file_write.write(formatted_json_stat_book)
                
statistiques()

