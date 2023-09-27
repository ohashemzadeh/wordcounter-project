from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {})


def counter(request):
    if request.method == 'POST':
        template_name: str = 'counter.html'
        txt: str = request.POST.get('mytext')
        characters_count: int = len(txt)
        words: list = txt.split(' ')

        # Counting repetition of each word
        words_repetition = {}
        for word in words:
            if word in words_repetition:
                words_repetition[word] += 1
                continue
            words_repetition[word] = 1

        # Sorting the dictionary
        words_repeat = {k: v for k, v in sorted(words_repetition.items(), key=lambda item: item[1])}

        context = {
            'txt': txt,
            'word_count': len(words),
            'unique_words_count': len(set(words)),
            'characters_count': characters_count,
            'words_repeat': words_repeat.items()
        }
        print(txt)
        return render(request, template_name, context)

    return HttpResponse('<a href="/">Please getback and enter some text </a>')


def about(request):
    return render(request, 'about.html', {})
