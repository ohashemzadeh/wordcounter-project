from django.http import HttpResponse
from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'homepage.html' , {} )

def counter(request):

    if request.method =='POST':
        template_name = 'counter.html'
        txt = request.POST.get('mytext')
        characters_count = len(txt)
        words = txt.split(' ')

        # Counting repetition of each word
        words_repeat = {}
        for word in words :
            if word in words_repeat:    # if word is in dictionary right now, add 1 count to it
                words_repeat[word] +=1
            else:   # if word is not in dictionary right now, add it to dictionary
                words_repeat[word] = 1

        # words_repeat =  i,j in sorted(words_repeat.keys())
        words_repeat = {k: v for k, v in sorted(words_repeat.items(), key=lambda item: item[1])}  # Sorting dictionary

        context = { 'txt':txt,
                    'word_count' : len(words),
                    'characters_count': characters_count,
                    'words_repeat' : words_repeat.items()
                    }
        print (txt)
        return render(request, template_name , context )

    else:
        return HttpResponse('<a href="/">Please getback and enter some text </a>')

def about(request):
    return render(request, 'about.html' , {} )