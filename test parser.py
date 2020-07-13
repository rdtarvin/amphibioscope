import sys
import xml.etree.ElementTree as ET
from lxml import html
import requests
import spacy


if len(sys.argv) >2:
    Genus = sys.argv[1]
    Species = sys.argv[2]
else:
   print("usage: "+sys.argv[0]+" <Genus_name> <Species_name>")
   print("running with default options")
   Genus = 'Phyllobates'
   Species = 'bicolor'

page = requests.get('https://amphibiaweb.org/cgi/amphib_ws?where-genus='+Genus+'&where-species='+Species+'&src=eol')
root = ET.fromstring(page.content)

for species in root.findall('species'):
    common_name = species.find('common_name')
    genus = species.find('genus')
    spec = species.find('species')
    print(genus.text.strip()+' '+spec.text.strip()+', also known as: '+common_name.text.strip())
    life_history = species.find('life_history')
    as_string = str(life_history.text.strip())
    print(as_string)

#load natural language processor
nlp = spacy.load(r'C:\Users\Tyler\Miniconda3\Lib\site-packages\en_core_web_sm\en_core_web_sm-2.3.1')

as_doc = nlp(as_string)

# print list of all individual tokens
for token in as_doc:
    print(token.text, token.pos)


#parse paragraph into sentences
sentences = list(as_doc.sents)

for sentence in sentences:
    print(sentence)


