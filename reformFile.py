import os
import re

def reformFile(corpus_path = "corpus_asimov_leaderboard", output_path = "corpus_reformed"):

    # Parcourir tous les répertoires du corpus
    for root, dirs, files in os.walk(corpus_path):
        for file in files:
            if file.endswith(".preprocessed"):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, corpus_path)
                output_folder = os.path.join(output_path, relative_path)
                output_file = os.path.join(output_folder, file.replace(".preprocessed", ""))

                # Créer le répertoire de sortie s'il n'existe pas
                os.makedirs(output_folder, exist_ok=True)

                # Pour les fichiers dans le dossier : corpus_path
                with open(input_file, "r", encoding="utf-8") as fichier_entree:
                    lignes = [ligne.strip() for ligne in fichier_entree.readlines()]
                    texte_combine = " ".join(lignes)

                # Pour les fichiers à créer dans le dossier : output_path
                with open(output_file, "w", encoding="utf-8") as fichier_sortie:
                    fichier_sortie.write(texte_combine)

                print(f"Le fichier {output_file} a été créé avec succès.")

    print("Tous les fichiers ont été traités.")
