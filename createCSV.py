# -*- coding: utf-8 -*-
import os
import spacy
import networkx as nx
import pandas as pd
import subprocess

print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
# Chargement du modèle SpaCy pour le français
nlp = spacy.load("fr_core_news_md")


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_characters(doc):
    characters = set()
    for ent in doc.ents:
        if ent.label_ == "PER" and ent.root.pos_ == "PROPN":
            characters.add(ent.text)
    return characters


def create_graph(characters, doc_ents):
    G = nx.Graph()
    for character in characters:
        G.add_node(character)
        # Ajout des alias spécifiques pour chaque personnage dans ce chapitre
        aliases = [ent.text for ent in doc_ents if ent.text != character and character in ent.text]
        unique_aliases = set(aliases)  # Utiliser un ensemble pour supprimer les doublons
        aliases_str = ';'.join([character] + list(unique_aliases)) if unique_aliases else character
        G.nodes[character]['names'] = aliases_str
    return G


def detect_co_occurrences(doc, G):
    co_occurrences = {}
    # Co-occurrences
    for i, token in enumerate(doc):
        if token.ent_type_ == "PER" and token.pos_ == "PROPN":
            # 25 tokens de différences
            for j in range(i + 1, min(i + 25, len(doc))):
                if doc[j].ent_type_ == "PER" and doc[j].pos_ == "PROPN" and token.text != doc[j].text:
                    co_occurrence = (token.text, doc[j].text)
                    if co_occurrence not in co_occurrences:
                        co_occurrences[co_occurrence] = 0
                    co_occurrences[co_occurrence] += 1

    for co_occurrence, freq in co_occurrences.items():
        character1, character2 = co_occurrence
        weight = freq
        # Poids de l'arête basé sur la fréquence de la co-occurrence
        if G.has_node(character1) and G.has_node(character2):
            # Ajout d'une arête entre les personnages en co-occurrence
            G.add_edge(character1, character2, weight=weight)

    return G


def process_chapter(chapter_path):
    text = read_text_file(chapter_path)
    doc = nlp(text)

    characters = extract_characters(doc)

    # Création du graphe pour le chapitre
    G = create_graph(characters, doc.ents)
    # Détection de co-occurrences
    G = detect_co_occurrences(doc, G)

    return G


def process_corpus(corpus_folder, book_folders):
    df_dict = {"ID": [], "graphml": []}

    G = nx.Graph()
    # Crée implicitement deux noeuds ("Hari" et "Dors"),
    # et ajoute un lien entre eux.
    G.add_edge("Hari", "Dors")
    # On ajoute les attributs "names"
    G.nodes["Hari"]["names"] = "Hari Seldon;Hari"
    G.nodes["Dors"]["names"] = "Dors;docteur Dors"
    df_dict["ID"].append("{}{}".format("lca", 0))
    graphml = "".join(nx.generate_graphml(G))
    df_dict["graphml"].append(graphml)
    df = pd.DataFrame(df_dict)
    df.set_index("ID", inplace=True)
    df.to_csv("./test.csv")


# Chemin vers le dossier contenant les fichiers texte
corpus_folder = "corpus_reformed"

# Liste des sous-dossiers pour chaque livre
book_folders = ["les_cavernes_d_acier", "prelude_a_fondation"]

# Pour chaque fichier des sous-dossiers, convertie les données et les inclue dans un CSV
process_corpus(corpus_folder, book_folders)