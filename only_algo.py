import nltk
import random
from nltk import RegexpParser, pos_tag

sentence = open('text.txt', 'r')
sentence = sentence.read()

tokens = nltk.word_tokenize(sentence)

tagged = pos_tag(tokens)

chunker = RegexpParser("""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """)

output = chunker.parse(tagged)

# Looking for NPs
nps = []
for subtree in output.subtrees():
    if subtree.label() == 'NP':
        np = ' '.join(word for word, tag in subtree.leaves())
        nps.append(np)

        
random.shuffle(nps)
print(nps)


