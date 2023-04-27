from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
import nltk
import random
from nltk import RegexpParser, pos_tag
# Create your views here.

def home(request):
    form = InputForm()
    return render(request, 'index.html', {'form': form })


def home(request):
    text = ''
    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['post']
            tokens = nltk.word_tokenize(text)

            tagged = pos_tag(tokens)

            chunker = RegexpParser("""
            NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
            PP: {<IN><NP>}               # Chunk prepositions followed by NP
            VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
            CLAUSE: {<NP><VP>}           # Chunk NP, VP
            """)

            output = chunker.parse(tagged)

            nps = []
            for subtree in output.subtrees():
                if subtree.label() == 'NP':
                    np = ' '.join(word for word, tag in subtree.leaves())
                    nps.append(np)

            random.shuffle(nps)

            text = nps
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form, 'text': text})