import matplotlib.pyplot as plt
import numpy as np
import os
import json

def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def drawData(chapterName):
    
    all_arr = []
    
    # les_cavernes_d_acier
    # prelude_a_fondation
    
    checkAndCreateFoldert("corpus/corpus_plots/")
    
    
    for file_name in os.listdir(f"corpus/corpus_statistiques/{chapterName}/"):
        file_path = f"corpus/corpus_statistiques/{chapterName}/" + file_name
        if file_path != f"corpus/corpus_statistiques/{chapterName}/statistique_of_book.json":
            with open(file_path, 'r', encoding='utf-8') as file_read:
                data = json.load(file_read)
                array_entityname_per_context = data["entityName_in_context"]["data"]
                
                all_arr.append(array_entityname_per_context)
            
    draw2Dplot(all_arr, f"Entity name in {chapterName}")
    

def cut_chunk(elements, n):
    out = []
    for i in range(0, n):
        out.append(elements[i::n])
    return out

def AverageNorm(vector, n):
    chunks = cut_chunk(vector, n)
    return [sum(c) / len(c) for c in chunks]

def draw2Dplot(all_arr, title):
    
    max_len = max([len(a) for a in all_arr])
    min_len = min([len(a) for a in all_arr])
    
    max_value = max([max(a) for a in all_arr])
    min_value = min([min(a) for a in all_arr])
    
    print(max_value)
    print(min_value)
    
    Z = np.array([
        a+[0]*(max_len-len(a))  for a in all_arr 
        # AverageNorm(a,    min_len) for a in all_arr 
    ])

    fig, ax0 = plt.subplots()
    ax0.pcolor(Z, cmap='gist_yarg', vmin=0, vmax=7) 
    
    ax0.set_title(title) 
    ax0.set_xlabel("Fenêtres dans le chapitre")
    ax0.set_ylabel("Chapitres")
    plt.savefig(f"./corpus/corpus_plots/{title}.png")

drawData("les_cavernes_d_acier")
drawData("prelude_a_fondation")