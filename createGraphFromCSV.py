# -*- coding: utf-8 -*-
import os
import pandas as pd

def createGraphFromCSV():

    # Charger le fichier CSV
    df = pd.read_csv("./my_submission.csv")

    # Créer le dossier s'il n'existe pas déjà
    output_folder = "./graphGenerated"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Pour chaque ligne du DataFrame
    for idx, row in df.iterrows():
        # Récupérer l'ID et le contenu graphml
        file_id = row['ID']
        graphml_content = row['graphml']

        # Créer le fichier .graphml avec l'ID comme nom de fichier
        file_path = os.path.join(output_folder, f"{file_id}.graphml")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(graphml_content)
