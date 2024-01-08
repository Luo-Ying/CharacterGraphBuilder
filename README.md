# CharacterGraphBuilder

Ce code est développé par :

* Jérôme BURGEAT
* Yingqi LUO

### Pré-requis

Python (version 3.9.13)

Dépendances Python (voir requirements.txt)

### Exécution du projet

_Assurez-vous d'avoir votre corpus dans le dossier corpus/[votre-dossier]_

Lancer la commande : **make run**

Le makefile contient : 

* python3 reformFile.py
* sh treatFileWithFreeling.sh
* python3 main.py

### `reformFile.py`

_Assurez-vous de spécifier les chemins corrects pour corpus_path et output_path avant d'exécuter ce script._

Le script vise à reformater les fichiers textuels du corpus en combinant leur contenu en un seul fichier par dossier.

Le script prend deux paramètres optionnels : 
* corpus_path (chemin vers le corpus initial)
* *output_path (chemin vers le dossier où seront placés les fichiers reformés). Si aucun chemin n'est spécifié, les valeurs par défaut sont utilisées (corpus/corpus_asimov_leaderboard pour le corpus initial et corpus/corpus_reformed pour le dossier de sortie).

Pour chaque fichier .preprocessed trouvé dans les sous-répertoires du corpus_path :
* Il combine le contenu de ce fichier en une seule chaîne de texte.
* Il crée un nouveau fichier dans le dossier spécifié par output_path, en écrivant cette chaîne de texte.

### `treatFileWithFreeling`

Pour chaque sous-dossier dans corpus/corpus_reformed et pour chaque fichier de ces sous-dossiers :
traite le fichier avec Freeling

### `main.py`

Ce script main.py est un programme Python qui effectue plusieurs opérations sur des données textuelles. Il utilise plusieurs fonctions définies dans d'autres fichiers pour réaliser les tâches suivantes :

1. **findEntityName()** : Identifie les noms d'entités dans les données textuelles.
2. **lemmatisationInCorpus()** : Applique une lemmatisation au corpus de texte.
3. **buildTokensInFiles()** : Construit des jetons (tokens) à partir des fichiers.
4. **createCSV()** : Crée un fichier CSV à partir des données traitées.
5. **createGraphFromCSV()** : Génère un graphe à partir du fichier CSV généré.

Les scripts peuvent être exécutés individuellement.

### `findEntityName.py`

_Ce script nécessite des modèles spécifiques pour Spacy et Camembert. Veuillez vous assurer que les modèles sont téléchargés et accessibles au script avant de l'exécuter sur vos propres données._

Ce script Python est conçu pour traiter des fichiers textuels en identifiant des entités nommées à l'aide de différentes méthodes telles que Spacy, Freeling, Camembert, et NLTK. 
Le script crée également des fichiers de résultats pour chaque méthode de traitement dans des dossiers spécifiques.

Il effectue les actions suivantes :

* Utilisation de modèles Spacy pour l'identification des entités nommées.
* Utilisation du modèle Camembert pour la reconnaissance d'entités.
* Utilisation de NLTK pour l'étiquetage de parties du discours et l'extraction des entités nommées. 

On intègre une fusion des résultats des traitements Spacy et Freeling pour identifier les entités communes.

### `removeEmptyWord.py`

_Le script peut nécessiter des ajustements de chemin ou de configuration en fonction de l'emplacement des fichiers à traiter. Veuillez vous assurer que les chemins sont correctement spécifiés dans le script avant de l'exécuter sur vos propres données._

Ce script traite les fichiers textuels en éliminant les mots vides et en retirant les ponctuations. 

Il effectue les opérations suivantes :

* Suppression des mots vides et des ponctuations des fichiers textuels. 
* Utilisation d'étiquettes morphosyntaxiques pour identifier les mots utiles basés sur leur nature (noms, adverbes, verbes, nombres, dates, etc.).

### `buildTokens.py`

Le script buildTokens.py est un programme Python conçu pour générer des tokens à partir de fichiers textuels prétraités. 

Il effectue les opérations suivantes :

* Construction de tokens en extrayant des mots spécifiques de fichiers textuels.
* Les tokens sont générés en regroupant 25 mots successifs dans un nouveau fichier, éliminant les espaces vides et les lignes vides.
Le script utilise des dossiers spécifiques pour lire les fichiers textuels prétraités à partir desquels il génère les tokens dans de nouveaux fichiers.

Assurez-vous que les chemins spécifiés dans le script correspondent aux emplacements corrects des fichiers d'entrée et de sortie avant de l'exécuter sur vos propres données. Vous pouvez également ajuster le nombre de mots utilisés pour générer les tokens en modifiant la valeur 25 dans le script.

### `createCSV.py`

_Assurez-vous que les chemins spécifiés dans le script correspondent aux emplacements corrects des fichiers d'entrée avant de l'exécuter sur vos propres données. Le fichier CSV résultant sera nommé my_submission.csv dans le répertoire actuel où le script est exécuté._

Le script createCSV.py est un programme Python qui construit des graphes à partir de fichiers texte et génère un fichier CSV représentant ces graphes. Il réalise les opérations suivantes :

1. Extraction des personnages des fichiers texte.
2. Construction d'un graphe basé sur les co-occurrences des personnages dans les fichiers textuels. 
3. Enregistrement des graphes dans un format GraphML. 
4. Conversion des graphes en un fichier CSV.

Le script utilise des dossiers spécifiques pour extraire les personnages des fichiers Freeling&Spacy et pour obtenir les tokens à partir des fichiers de corpus de tokens.

### `createGraphFromCSV.py`

_Pour utiliser ce script, assurez-vous d'avoir le fichier CSV `my_submission.csv` généré par `createCSV.py` dans le même répertoire. Le script créera un dossier `graphGenerated` et y sauvegardera les fichiers .graphml correspondants à chaque ligne du CSV._

Ce script lit le fichier CSV généré par `createCSV.py`.

Puis ce dernier crée des fichiers .graphml à partir des données du CSV, et les stocke dans un dossier spécifique.