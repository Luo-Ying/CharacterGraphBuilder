import os
import networkx as nx

# Fonction pour extraire les personnages d'un fichier donné
def extract_characters(file_path):
    characters = []
    with open(file_path, 'r') as file:
        for line in file:
            characters.extend(line.strip().split())  # Sépare les tokens pour obtenir les entités
    return set(characters)  # Utilisation d'un ensemble pour éviter les doublons


# Fonction pour construire le graphe pour un chapitre donné
def build_graph(characters, tokens):
    G = nx.Graph()
    characters_mapping = {}  # Pour stocker les alias de chaque personnage

    for character in characters:
        characters_mapping[character] = [character.lower()]  # Initialise avec le nom du personnage

    for i, token in enumerate(tokens[:-1]):  # Correction ici pour éviter l'index out of range
        for character in characters:
            if character.lower() in token.lower():
                for other_character in characters:
                    if other_character != character and other_character.lower() in tokens[i + 1].lower():
                        # Co-occurrence détectée, met à jour les alias
                        characters_mapping[character].extend(characters_mapping[other_character])
                        characters_mapping[character] = list(set(characters_mapping[character]))  # Supprime les doublons

    for character, aliases in characters_mapping.items():
        aliases_str = ";".join(aliases)
        G.add_node(character, names=aliases_str)  # Ajoute le nœud avec la liste d'alias

    # Analyse des co-occurrences des entités dans les 25 tokens suivants
    for i, token in enumerate(tokens[:-1]):  # Correction ici pour éviter l'index out of range
        for character in characters:
            if character.lower() in token.lower():
                for j in range(i + 1, min(i + 26, len(tokens))):
                    for other_character in characters:
                        if other_character != character and other_character.lower() in tokens[j].lower():
                            if G.has_edge(character, other_character):
                                G[character][other_character]['weight'] += 1
                            else:
                                G.add_edge(character, other_character, weight=1)

    # Suppression des liens entre un personnage et lui-même
    for character in characters:
        if G.has_edge(character, character):
            G.remove_edge(character, character)

    return G


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

        # Lecture des tokens du corpus tokens
        tokens_file_path = os.path.join(tokens_folder, f'{book_folder}/chapter_{chapter+1}.txt')
        with open(tokens_file_path, 'r') as file:
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