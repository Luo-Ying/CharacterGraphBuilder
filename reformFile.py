import re

input_file = "D:\CoursAmphi\MASTER\S3\Innovation\CharacterGraphBuilder\corpus_asimov_leaderboard\les_cavernes_d_acier\chapter_1.txt.preprocessed"  # Remplacez par le chemin de votre fichier d'entrée
output_file = "D:\CoursAmphi\MASTER\S3\Innovation\CharacterGraphBuilder\corpus_asimov_leaderboard\les_cavernes_d_acier\output.txt"  # Remplacez par le chemin de votre fichier de sortie

# Ouvrir le fichier texte en mode lecture
with open(input_file, "r", encoding="utf-8") as fichier_entree:
    # Lire le contenu du fichier ligne par ligne et supprimer les sauts de ligne
    lignes = [ligne.strip() for ligne in fichier_entree.readlines()]

# Combinez toutes les lignes en une seule ligne avec des espaces entre les mots
texte_combine = " ".join(lignes)

# Divisez la chaîne en phrases en utilisant des caractères de ponctuation
# phrases = re.split(r'(?<=[.!?])\s', texte_combine)

# Réassemblez les phrases avec des sauts de ligne
# nouveau_texte = '\n'.join(phrases)

# Ouvrir un nouveau fichier en mode écriture
with open(output_file, "w", encoding="utf-8") as fichier_sortie:
    # Écrire le texte combiné avec des sauts de ligne à chaque ponctuation dans le nouveau fichier
    fichier_sortie.write(texte_combine)
    # fichier_sortie.write(nouveau_texte)

print("Le fichier a été créé avec succès, avec des sauts de ligne à chaque ponctuation.")


