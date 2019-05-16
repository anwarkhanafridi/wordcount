from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'name': 'Hi there is Anwarkhan '})


def contact(request):
    return HttpResponse('<h2> contact page</h2><br> this is ourHOHO contact page')

def my_try(request):
    return render(request, 'home.html', {'try':'this another page'})

def count(request):
    data = request.GET['fulltextarea']
    #print(data)   # here we get data in show in with terminal
    word_list = data.split() # separte word in terminal
    #print(word_list)
    len_word = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            #increase value by 1
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
            # add to the worddictionary and set value to 1

    sorted_list = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': data, 'len_word': len_word, 'worddictionary': sorted_list})

def about(request):
    return render (request, 'about.html', {'about': 'hi, this page about me'})