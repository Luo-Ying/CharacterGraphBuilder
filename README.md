# CharacterGraphBuilder

Ce code est développé par :

* Jérôme BURGEAT
* Yingqi LUO

Pour réaliser un graphe qui lit les personnages d'un chapitre d'un livre, il faut tout d'abord utiliser le fichier suivant :

### `createCSV.py`

Ce script Python permet d'extraire des réseaux de personnages à partir du corpus Fondation en utilisant SpaCy pour l'identification des entités nommées et NetworkX pour la construction des graphes. 

Il se divise en plusieurs fonctions pour chaque étape du processus :

1. **read_text_file** : Lit un fichier texte.
2. **resolve_alias** : Résout les alias des personnages.
3. **extract_characters** : Extrait les entités de type "personne" du texte.
4. **create_graph** : Crée un graphe à partir des personnages.
5. **detect_co_occurrences** : Détecte les co-occurrences entre les personnages et pondère les arêtes en fonction de la fréquence.
6. **process_chapter** : Processus global pour chaque chapitre du corpus.
7. **process_corpus** : Processus global pour livre du corpus.

Pour utiliser ce script, il suffit de spécifier le chemin du corpus et des sous-dossiers pour chaque livre, puis d'appeler la fonction ___process_corpus___.

### `createGraphFromCSV.py`

Ce script lit le fichier CSV généré par `createCSV.py`.

Puis ce dernier crée des fichiers .graphml à partir des données du CSV, et les stocke dans un dossier spécifique.

Pour utiliser ce script, assurez-vous d'avoir le fichier CSV `my_submission.csv` généré par `createCSV.py` dans le même répertoire. Le script créera un dossier `graphGenerated` et y sauvegardera les fichiers .graphml correspondants à chaque ligne du CSV.

### Attention
Ces scripts peuvent être exécutés individuellement pour extraire les réseaux de personnages et générer les fichiers .graphml correspondants pour une analyse ultérieure. Assurez-vous d'avoir les bibliothèques Python nécessaires installées pour exécuter ces scripts :

* spacy
* networkx
* pandas
* subprocess