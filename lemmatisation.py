import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def tokeniser_et_nettoyer(texte):
    # Tokeniser le texte en mots
    mots = word_tokenize(texte, language='french')  # Utiliser 'english' si votre texte est en anglais

    # Charger la liste des "stop words" en français
    stop_words = set(stopwords.words('french'))

    # Enlever les mots inutiles
    mots_filtres = [mot for mot in mots if mot.lower() not in stop_words]

    return mots_filtres

with open('corpus_asimov_leaderboard/les_cavernes_d_acier/output.txt') as file:
    file_content = file.read()

texte = file_content
tokens_propres = tokeniser_et_nettoyer(texte)
print(tokens_propres)
