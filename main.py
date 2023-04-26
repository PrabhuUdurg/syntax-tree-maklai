import nltk
from nltk import RegexpParser, pos_tag

sentence = open('text.txt', 'r')
sentence = sentence.read()

tokens = nltk.word_tokenize(sentence)

tagged = pos_tag(tokens)

chunker = RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                       P: {<IN>}               #To extract Prepositions
                       V: {<V.*>}              #To extract Verbs
                       PP: {<p> <NP>} 
                       VP: {<V> <NP|PP>*}      #To extract Verb Phrases
                       """)

output = chunker.parse(tagged)
