import nltk
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
