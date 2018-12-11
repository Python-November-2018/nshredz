from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, "surveys/index.html")

def process(request):
    if not 'total' in request.session:
        request.session['total'] = 1
    else:
        request.session['total'] += 1
    
    print(request.POST)
    city = {
        "chicago": "Chicago, IL",
        "dallas": "Dallas, TX",
        "new_york": "New York, NY",
        "seattle": "Seattle, WA"
    }
    lang = {
        "clipper": "Clipper",
        "fortran": "FORTRAN",
        "python": "Python",
        "smalltalk": "Smalltalk"
    }

    errors = []
    
    if len(request.POST['name']) < 3:
        errors.append('Name must be at least three characters long.')
    
    request.session['name'] = request.POST['name']
    city_name = city[request.POST['location']]
    lang_name = lang[request.POST['language']]
    request.session['location'] = city_name
    request.session['language'] = lang_name
    request.session['comment'] = request.POST['comment']
    
    if len(errors) > 0:
        print('*' * 80)
        print(request.session['comment'])
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    
    return redirect("/result/")

def result(request):
    return render(request, "surveys/result.html")