# -*- coding: utf-8 -*-
import os
import networkx as nx

# Fonction pour extraire les personnages d'un fichier donné
def extract_characters(file_path):
    characters = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line.strip().split()[0]) > 1 and line.strip().split()[0] not in stopwords:
                characters.append(line.strip().split()[0])
    return set(characters)  # Utilisation d'un ensemble pour éviter les doublons


# Fonction pour construire le graphe pour un chapitre donné
def build_graph(characters, tokens):
    G = nx.Graph()
    characters_mapping = {}  # Pour stocker les alias de chaque personnage

    for character in characters:
        characters_mapping[character] = [character]  # Initialise avec le nom du personnage

    for i, token in enumerate(tokens):  # Correction ici pour éviter l'index out of range
        for character in characters:
            if character in token:
                for other_character in characters:
                    if character.lower() in other_character.lower() or other_character.lower() in character.lower() :
                        # Co-occurrence détectée, met à jour les alias
                        characters_mapping[character].extend(characters_mapping[other_character])
                        characters_mapping[character] = list(set(characters_mapping[character]))  # Supprime les doublons

    for character, aliases in characters_mapping.items():
        aliases_str = ";".join(aliases)
        if aliases_str.strip():  # Vérifie si le contenu de l'alias n'est pas vide
            existing_nodes = [node for node, data in G.nodes(data=True) if
                              data.get('names') == aliases_str.replace('_', ' ')]
            if existing_nodes:
                continue
            else:
                G.add_node(character.replace('_', ' '), names=aliases_str.replace('_', ' '))

    # Analyse des co-occurrences des entités dans les 25 tokens suivants
    for i, token in enumerate(tokens):
        for character in characters:
            if character.lower() in token.lower():
                for j in range(i + 1, min(i + 26, len(tokens))):
                    for other_character in characters:
                        if other_character != character and other_character.lower() in tokens[j].lower():
                            if character in G.nodes and other_character in G.nodes:
                                # Vérifier si le personnage est un alias d'un autre
                                if character.lower() in [alias.lower() for alias in characters_mapping[other_character]] \
                                        or other_character.lower() in [alias.lower() for alias in
                                                                       characters_mapping[character]]:
                                    # Si oui, incrémenter le poids vers le nœud parent
                                    parent_node = [alias for alias in characters_mapping.keys() if
                                                   character.lower() != alias.lower() and
                                                   other_character.lower() in [a.lower() for a in
                                                                               characters_mapping[alias]]][0]
                                    if G.has_edge(parent_node, other_character):
                                        G[parent_node][other_character]['weight'] += 1

                                else:
                                    # Sinon, ajouter un edge entre les personnages s'ils ne sont pas dans leurs alias
                                    if character not in characters_mapping[other_character] and other_character not in \
                                            characters_mapping[character]:
                                        if G.has_edge(character, other_character):
                                            G[character][other_character]['weight'] += 1
                                        else:
                                            G.add_edge(character, other_character, weight=1)

    # Suppression des liens entre un personnage et lui-même
    for character in characters:
        if G.has_edge(character.replace('_', ' '), character.replace('_', ' ')):
            G.remove_edge(character.replace('_', ' '), character.replace('_', ' '))

    return G

def createCSV():
    # Mots à exclure
    stopwords = []
    with open("stopWords", 'r', encoding='utf-8') as file:
        for line in file:
            stopwords.append(line.replace('\n', ''))

    # Dossiers contenant les fichiers
    freeling_spacy_folder = 'corpus_treated_merge_of_Freeling&Spacy'
    tokens_folder = 'corpus_tokens'

    books = [
        (list(range(0, 18)), "lca", "les_cavernes_d_acier"),
        (list(range(0, 19)), "paf", "prelude_a_fondation"),
    ]
    df_dict = {"ID": [], "graphml": []}

    for chapters, book_code, book_folder in books:
        for chapter in chapters:
            # Lecture des personnages du corpus Freeling&Spacy
            characters_file_path = os.path.join(freeling_spacy_folder, f'{book_folder}/chapter_{chapter+1}.txt')
            characters = extract_characters(characters_file_path)
            # print(characters)

            # Lecture des tokens du corpus tokens
            tokens_file_path = os.path.join(tokens_folder, f'{book_folder}/chapter_{chapter+1}.txt_whithout_punctuation.txt')
            with open(tokens_file_path, 'r', encoding='utf-8') as file:
                tokens = file.read().split()

            # Construction du graphe
            graph = build_graph(characters, tokens)

            # Enregistrement du graphe au format GraphML
            graphml = "".join(nx.generate_graphml(graph))
            df_dict["ID"].append(f"{book_code}{chapter}")
            df_dict["graphml"].append(graphml)

    # Conversion en DataFrame et sauvegarde en CSV
    import pandas as pd
    df = pd.DataFrame(df_dict)
    df.set_index("ID", inplace=True)
    df.to_csv("./my_submission.csv")