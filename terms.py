from TermNode import *
from NodeCollection import *

# get filenames from directory
# trim filenames and append directory containing it

with open("filenames/drugbank filenames") as f:
    drugbank_filenames = f.readlines()

for i in range(len(drugbank_filenames)):
    drugbank_filenames[i] = "DrugBank/" + drugbank_filenames[i]

with open("filenames/medline filenames") as f:
    medline_filenames = f.readlines()

for i in range(len(medline_filenames)):
    medline_filenames[i] = "MedLine/" + medline_filenames[i]

# create node collections, parse files

drugbank = NodeCollection(drugbank_filenames)
drugbank.make_corpus()

medline = NodeCollection(medline_filenames)
medline.make_corpus()