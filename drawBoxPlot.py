import matplotlib.pyplot as plt
import numpy as np
import json
import os

def drawBoxPlot(title, data, x_label, y_label):
    
    plt.boxplot(data)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xticks(range(len(x_label)), x_label)
    plt.savefig(f"./corpus/corpus_plots/{title}.png")
    plt.show()
    

def drawSubplots(data, title, x_label, y_label):
    
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(data)), data, color='b', alpha=0.6, label="Data")
    
    plt.title(title)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label, color='b')
    
    plt.savefig(f"./corpus/corpus_plots/{title}.png")


def checkAndCreateFoldert(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def drawData(fileStatistique):
    
    checkAndCreateFoldert("corpus/corpus_plots/")
    
    with open(fileStatistique, 'r', encoding='utf-8') as file_read:
        data = json.load(file_read)

            
    text = fileStatistique.split('/')
    title = text[2] + '-' + text[3]
            
    drawBoxPlot(f"{title}-boxplot_entityname", [data["entityName_in_context"]["data"]], ["x", "Nombre de entity name par context"], "Nombre de entity name")
    
    drawBoxPlot(f"{title}-boxplot_words", [data["words_in_phrase"]["data"], data["words_in_paragraph"]["data"]], ["x", "Mots dans les phrase", "Mots dans les paragraphs"], "Nombre de mots")
    
    drawSubplots(data["words_in_phrase"]["data"], f"{title}-barChart_wordsOfPhrase", "Nombre de phrase", "Nombre de mots")
    
    drawSubplots(data["words_in_paragraph"]["data"], f"{title}-barChart_wordsOfParagraph", "Nombre de paragraph", "Nombre de mots")
    
    drawSubplots(data["entityName_in_context"]["data"], f"{title}-barChart_entityName", "Nombre de context", "Nombre de entity name")
    

drawData("corpus/corpus_statistiques/les_cavernes_d_acier/chapter_1.txt.json")