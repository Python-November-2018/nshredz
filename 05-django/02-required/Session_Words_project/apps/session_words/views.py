from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime

def index(request):

    return render(request, "session_words/index.html")

def add(request):
    errors = []
    
    if len(request.POST['word']) < 3:
        errors.append('Name must be at least three characters long.')
        for error in errors:
            messages.error(request, error)
        return redirect('/')

    print(request.POST)
    font = '175%' if 'big_font' in request.POST else '100%'
    if not 'data' in request.session:
        request.session['data'] = []
    temp_list = request.session['data']
    temp_list.append({
        "word": request.POST['word'],
        "color": request.POST['color'],
        "font": font,
        "time": strftime("%b-%d-%Y %H:%M %p", localtime())
    })
    print(f'Temp List: {temp_list}')
    request.session['data'] = temp_list
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")