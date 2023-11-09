from pprint import pprint
import spacy
import subprocess
print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
nlp_fr = spacy.load('fr_core_news_md')
text = (''' Le texte à enter''')
doc = nlp_fr(text)
pprint([(word.text, word.label_) for word in doc.ents])
