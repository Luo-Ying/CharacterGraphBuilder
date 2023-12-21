from pprint import pprint
import spacy
import subprocess
# import fr_core_news_lg
import os
from pathlib import Path


def useModelSpacy(nlp, file_to_read, file_spacy_result):

    with open(file_to_read) as file:
        file_content = file.read()

    doc = nlp(file_content)

    persons = [(word.text, word.label_) for word in doc.ents if word.label_ == 'PER']

    results = [(word.text, word.label_) for word in doc.ents]

    with open(file_spacy_result, 'w') as output_file:
        for item in results:
            item1 = item[0].replace('\n', ' ')
            item1 = item1.replace(' ', '_')
            item2 = item[1].replace('\n', ' ')
            item2 = item2.replace(' ', '_')
            output_file.write(f'{item1} {item2}\n')


def useFreeling(file_freeling_result):

    with open(file_freeling_result, 'r') as file:
        lines = file.readlines()

    filtered_PER = [line for line in lines if len(line.split()) >= 3 and line.split()[2] == "NP00000"]
        
    with open(file_freeling_result, 'w') as file:
        file.writelines(filtered_PER)

    
def mergeResult(file_freeling_result, file_spacy_result, file_merge_results_of_2_models):
    with open(file_freeling_result) as file:
        file_freeling_result_content = file.readlines()

    with open(file_spacy_result) as file:
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




    with open(file_merge_results_of_2_models, 'w') as file:
        file.writelines(filtered_PER)


def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        

def findEntityName():
    
    print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
    nlp = spacy.load("fr_core_news_md")
    # nlp_fr = fr_core_news_lg.load()
    
    checkAndCreateFoldert("corpus_treated_by_Spacy")
    
    path = Path("corpus_reformed")
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for dir in subdirectories:
        if os.path.exists("corpus_treated_by_Spacy/" + dir)==False: os.makedirs("corpus_treated_by_Spacy/" + dir)
        files = os.listdir("corpus_reformed/" + dir)
        for file in files:
            file_to_read = "corpus_reformed/" + dir + "/" + file
            file_spacy_result = "corpus_treated_by_Spacy/" + dir + "/" + file
            
            useModelSpacy(nlp, file_to_read, file_spacy_result)
            
    folder_freeling_result = "corpus_treated_by_Freeling/"
    folder_spacy_result = "corpus_treated_by_Spacy/"
    
    folder_merge = "corpus_treated_merge_of_Freeling&Spacy/"
    
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
    
    
findEntityName()