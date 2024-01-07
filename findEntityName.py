import spacy
# import fr_core_news_lg
import os
import subprocess
from pathlib import Path

import spacy
from nltk.tag import StanfordPOSTagger
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def useModelSpacy(nlp, file_to_read, file_spacy_result):

    with open(file_to_read, 'r', encoding='utf-8') as file:
        file_content = file.read()

    doc = nlp(file_content)

    persons = [(word.text, word.label_) for word in doc.ents if word.label_ == 'PER']

    results = [(word.text, word.label_) for word in doc.ents]

    with open(file_spacy_result, 'w', encoding='utf-8') as output_file:
        for item in results:
            item1 = item[0].replace('\n', ' ')
            item1 = item1.replace(' ', '_')
            item2 = item[1].replace('\n', ' ')
            item2 = item2.replace(' ', '_')
            output_file.write(f'{item1} {item2}\n')


def useFreeling(file_freeling_result):

    with open(file_freeling_result, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_PER = [line for line in lines if len(line.split()) >= 3 and line.split()[2] == "NP00000"]
        
    with open(file_freeling_result, 'w', encoding='utf-8') as file:
        file.writelines(filtered_PER)

def useModelCamembert(model, tokenizer, file_to_read, file_camembert_result):
    with open(file_to_read, 'r', encoding='utf-8') as file:
        file_content = file.read()

    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    personnages = nlp(file_content)

    persons = [(person['word'], person['entity_group']) for person in personnages if person['entity_group'] == 'PER']

    with open(file_camembert_result, 'w', encoding='utf-8') as output_file:
        for item in persons:
            item1 = item[0].replace('\n', ' ')
            item1 = item1.replace(' ', '_')
            item2 = item[1].replace('\n', ' ')
            item2 = item2.replace(' ', '_')
            output_file.write(f'{item1} {item2}\n')

def useNLTK(file_to_read, file_nltk_result):
    with open(file_to_read, 'r', encoding='utf-8') as file:
        file_content = file.read()

    jar = './stanford-postagger-full-2020-11-17/stanford-postagger.jar'
    model = './stanford-postagger-full-2020-11-17/models/french-ud.tagger'
    os.environ['JAVAHOME'] = './jdk1.8.0_161/bin/java.exe' #

    blob = (file_content)

    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
    res = pos_tagger.tag(blob.split())
    persons = [tup for tup in res if tup[1] == 'PROPN']

    with open(file_nltk_result, 'w', encoding='utf-8') as output_file:
        for item in persons:
            item1 = item[0].replace('\n', ' ')
            item1 = item1.replace(',', '')
            item1 = item1.replace('...', '')
            item1 = item1.replace('.', '')
            item1 = item1.replace('\'', '')
            item1 = item1.replace('’', '')
            item1 = item1.replace(' ', '_')
            item2 = item[1].replace('\n', ' ')
            item2 = item2.replace(' ', '_')
            output_file.write(f'{item1} {item2}\n')

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

    
def mergeResult(file_freeling_result, file_spacy_result, file_merge_results_of_2_models):
    with open(file_freeling_result, 'r', encoding='utf-8') as file:
        file_freeling_result_content = file.readlines()

    with open(file_spacy_result, 'r', encoding='utf-8') as file:
        file_spacy_result_content = file.readlines()


    filtered_PER_exist = []
    for item_freeling_result in file_freeling_result_content:
        
        exist = False
        for item_spacy_result in file_spacy_result_content:
            if bool(item_freeling_result.strip()) and bool(item_spacy_result.strip()) and item_freeling_result.split()[0] == item_spacy_result.split()[0]:
                exist = True
                break
        
        if exist == True:
            filtered_PER_exist.append(item_freeling_result)


    filtered_PER = []
    for person in filtered_PER_exist:
        isPerson = False
        for item_spacy_result in file_spacy_result_content:
            if (item_spacy_result.split()[0] == person.split()[0]) and (item_spacy_result.split()[1] == 'PER' or item_spacy_result.split()[1] == 'MISC'):
                isPerson = True
                break
        if isPerson == True:
            filtered_PER.append(person)




    with open(file_merge_results_of_2_models, 'w', encoding='utf-8') as file:
        file.writelines(filtered_PER)


def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def findEntityName():
    
    corpus_reformed ="corpus/corpus_reformed/"
    
    folder_spacy_result = "corpus/corpus_treated_by_Spacy/"
    folder_freeling_result = "corpus/corpus_treated_by_Freeling/"
    
    folder_merge = "corpus/corpus_treated_merge_of_Freeling&Spacy/"
    folder_camembert_result = "corpus/corpus_treated_by_Camembert/"
    folder_nltk_result = "corpus/corpus_treated_by_NLTK/"

    print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
    nlp = spacy.load("fr_core_news_md")
    # nlp_fr = fr_core_news_lg.load()

    tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")

    checkAndCreateFoldert(folder_spacy_result)
    checkAndCreateFoldert(folder_camembert_result)
    checkAndCreateFoldert(folder_nltk_result)

    path = Path(corpus_reformed)
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        if os.path.exists(folder_spacy_result + dir)==False: os.makedirs(folder_spacy_result + dir)
        if os.path.exists(folder_camembert_result + dir) == False: os.makedirs(folder_camembert_result + dir)
        if os.path.exists(folder_nltk_result + dir) == False: os.makedirs(folder_nltk_result + dir)
        files = os.listdir(corpus_reformed + dir)
        for file in files:
            file_to_read = corpus_reformed + dir + "/" + file
            file_spacy_result = folder_spacy_result + dir + "/" + file
            file_camembert_result = folder_camembert_result + dir + "/" + file
            file_nltk_result = folder_nltk_result + dir + "/" + file

            useModelSpacy(nlp, file_to_read, file_spacy_result)
            useModelCamembert(model, tokenizer, file_to_read, file_camembert_result)
            useNLTK(file_to_read, file_nltk_result)

    for dir in subdirectories:
        if os.path.exists(folder_merge + dir) == False: os.makedirs(folder_merge + dir)
        files_freeling = os.listdir(folder_freeling_result + dir)
        files_spacy = os.listdir(folder_spacy_result + dir)
        for file_freeling in files_freeling:
            for file_spacy in files_spacy:
                if file_freeling == file_spacy:
                    file_freeling_result_path = folder_freeling_result + dir + "/" + file_freeling
                    file_spacy_result_path = folder_spacy_result + dir + "/" + file_spacy
                    file_to_save_result_merge = folder_merge + dir + "/" + file_freeling
                    mergeResult(file_freeling_result_path, file_spacy_result_path, file_to_save_result_merge)