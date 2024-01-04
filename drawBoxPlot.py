import matplotlib.pyplot as plt
import numpy as np

def drawBoxPlot(title, data, x_label, y_label):
    
    plt.boxplot(data)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xticks(range(len(x_label)), x_label)
    plt.show()
    

def drawSubplots(data, title, x_label, y_label):
    
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(data)), data, color='b', alpha=0.6, label="Data")
    
    plt.title(title)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label, color='b')
    
    plt.show()
    

def drawData(fileStatistique):
    
    with open(fileStatistique, 'r', encoding='utf-8') as file_read:
        line = file_read.readline()
        while line:
            # print(line)
            if "mots_par_phrase" in line:
                elements = line.split(':')
                str_data = elements[1].strip("[] \n")
                array_words_per_phrase = [int(x) for x in str_data.split(", ")]
            if "mots_par_paragraph" in line:
                elements = line.split(':')
                str_data = elements[1].strip("[] \n")
                array_words_per_paragraph = [int(x) for x in str_data.split(", ")]
            if "entityname_par_context" in line:
                elements = line.split(':')
                str_data = elements[1].strip("[] \n")
                array_entityname_per_context = [int(x) for x in str_data.split(", ")]
            line = file_read.readline()
            
    text = fileStatistique.split('/')
    title = text[2] + '/' + text[3]
            
    drawBoxPlot(title, [array_words_per_phrase, array_words_per_paragraph], ["x", "Nombre de mots par phrase", "Nombre de mots par paragraph"], "Nombre de mots")
    
    drawBoxPlot(title, [array_entityname_per_context], ["x", "Nombre de entity name par context"], "Nombre de entity name")
    
    drawSubplots(array_words_per_phrase, title, "Nombre de phrase", "Nombre de mots")
    
    drawSubplots(array_words_per_paragraph, title, "Nombre de paragraph", "Nombre de mots")
    
    drawSubplots(array_entityname_per_context, title, "Nombre de context", "Nombre de entity name")
    

drawData("corpus/corpus_statistiques/les_cavernes_d_acier/chapter_1.txt")