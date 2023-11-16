from pprint import pprint
import spacy
import subprocess
print(subprocess.getoutput("python -m spacy download fr_core_news_md"))
nlp_fr = spacy.load('fr_core_news_md')
with open('corpus_asimov_leaderboard/les_cavernes_d_acier/output.txt') as file:
    file_content = file.read()
text = file_content
doc = nlp_fr(text)
pprint([(word.text, word.label_) for word in doc.ents if (word.label_ == 'PER' or word.label_ == 'MISC')])
