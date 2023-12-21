import os
import spacy
import networkx as nx
import pandas as pd
import subprocess

# print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
# Chargement du modèle SpaCy pour le français
nlp = spacy.load("fr_core_news_md")


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Alias (à voir comment le gérer manuellemenent)
def resolve_alias(characters):
    alias_resolution = {
        "John Traitor": "John",
        "Sir Traitor": "John",
        "Hari Seldon": "Hari",
        "Mr Seldon": "Hari",
        "Mme Seldon": "Hari"
    }
    resolved_characters = [alias_resolution.get(char, char) for char in characters]
    return resolved_characters


def extract_characters_md(doc):
    characters = set()
    for ent in doc.ents:
        if ent.label_ == "PER" and ent.root.pos_ == "PROPN":
            characters.add(ent.text)
    return characters


def create_graph(characters):
    G = nx.Graph()
    for character in characters:
        G.add_node(character)
        # Ajout de l'attribut 'names' avec le nom du personnage
        G.nodes[character]['names'] = character
    return G


def detect_co_occurrences(doc, G):
    co_occurrences = {}
    # Co-occurrences
    for i, token in enumerate(doc):
        if token.ent_type_ == "PER" and token.pos_ == "PROPN":
            # 25 tokens de differences
            for j in range(i + 1, min(i + 25, len(doc))):
                if doc[j].ent_type_ == "PER" and doc[j].pos_ == "PROPN":
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

    characters = extract_characters_md(doc)
    resolved_characters = resolve_alias(characters)
    # print(resolved_characters)

    # Création du graphe pour le chapitre
    G = create_graph(resolved_characters)
    # Détection de co-occurences
    G = detect_co_occurrences(doc, G)

    return G


def process_corpus(corpus_folder = "corpus_reformed", book_folders = ["les_cavernes_d_acier", "prelude_a_fondation"]):
    df_dict = {"ID": [], "graphml": []}

    for book_folder in book_folders:
        book_path = os.path.join(corpus_folder, book_folder)
        chapters = os.listdir(book_path)
        chapter_number = 0
        for chapter_file in chapters:
            chapter_path = os.path.join(book_path, chapter_file)

            G = process_chapter(chapter_path)

            # Génération du graphml
            graphml = "".join(nx.generate_graphml(G))
            if book_folder == "prelude_a_fondation":
                df_dict["ID"].append(f"paf{chapter_number}")
            else:
                df_dict["ID"].append(f"lca{chapter_number}")
            df_dict["graphml"].append(graphml)
            chapter_number += 1

    # Génération du CSV
    df = pd.DataFrame(df_dict)
    df.set_index("ID", inplace=True)
    df.to_csv("./my_submission.csv")


# # Chemin vers le dossier contenant les fichiers texte
# # corpus_folder = "corpus_asimov_leaderboard"
# corpus_folder = "corpus_reformed"

# # Liste des sous-dossiers pour chaque livre
# book_folders = ["les_cavernes_d_acier", "prelude_a_fondation"]

# # Pour chaque fichier des sous-dossiers, convertie les données et les inclue dans un CSV
# process_corpus(corpus_folder, book_folders)