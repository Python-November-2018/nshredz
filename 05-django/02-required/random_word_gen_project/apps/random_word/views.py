from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return redirect('/random_word')

def random_word(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    
    request.session['random_word'] = get_random_string(length=14)
    
    print('*' * 80)
    print(request.session['attempt'])
    print(request.session['random_word'])
    print('*' * 80)
    
    return render(request, "random_word/index.html", request.session)

def reset(request):
    del request.session['attempt']

    return redirect('/')