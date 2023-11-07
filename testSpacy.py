from pprint import pprint
import spacy
import fr_core_news_md
nlp_fr = fr_core_news_md.load()
text = (''' Le texte à enter''')
doc = nlp_fr(text)
pprint([(word.text, word.label_) for word in doc.ents])
