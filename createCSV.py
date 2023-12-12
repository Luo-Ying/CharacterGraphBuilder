import os
import spacy
import networkx as nx
import pandas as pd
import subprocess

print(subprocess.getoutput("python -m spacy download fr_core_news_md"))

# Chargement du modèle SpaCy pour le français
nlp_fr = spacy.load('fr_core_news_md')

# Chemin vers le dossier contenant les fichiers texte
corpus_folder = "corpus_asimov_leaderboard"

# Liste des sous-dossiers pour chaque livre
book_folders = ["les_cavernes_d_acier", "prelude_a_fondation"]

df_dict = {"ID": [], "graphml": []}

for book_folder in book_folders:
    book_path = os.path.join(corpus_folder, book_folder)
    chapters = os.listdir(book_path)

    for chapter_file in chapters:
        chapter_path = os.path.join(book_path, chapter_file)

        with open(chapter_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Création du graphe pour le chapitre
        G = nx.Graph()
        doc = nlp_fr(text)

        # Alias (à voir comment le gérer manuellemenent)
        alias_resolution = {
            "John Traitor": "John",
            "Sir Traitor": "John",
            "Hari Seldon": "Hari",
            "Mr Seldon": "Hari",
            "Mme Seldon": "Hari"
        }

        for ent in doc.ents:
            if ent.label_ == "PER":
                character = ent.text
                # Alias === PER ?
                if character in alias_resolution:
                    character = alias_resolution[character]
                G.add_node(character)
                # Ajout de l'attribut 'names' avec le nom du personnage
                G.nodes[character]['names'] = character

        # Co-occurrences
        for i, token in enumerate(doc):
            if token.ent_type_ == "PER":
                # 25
                for j in range(i + 1, min(i + 25, len(doc))):
                    if doc[j].ent_type_ == "PER":
                        # Ajout d'une arête entre les personnages en co-occurrence
                        if G.has_node(token.text) and G.has_node(doc[j].text):
                            G.add_edge(token.text, doc[j].text)

        # Génération du graphml
        graphml = "".join(nx.generate_graphml(G))
        df_dict["ID"].append(f"{book_folder}_{chapter_file.split('.')[0]}")
        df_dict["graphml"].append(graphml)

# Création du DataFrame et exportation au format CSV
df = pd.DataFrame(df_dict)
df.set_index("ID", inplace=True)
df.to_csv("./my_submission.csv")
