from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

def index(request):
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0
    if not 'activities' in request.session:
        request.session['activities'] = []

    return render(request, "gold/index.html")

def process_money(request):

    location_map = {
        "farm": random.randrange(10, 21),
        "cave": random.randrange(5, 11),
        "house": random.randrange(2, 6),
        "casino": random.randrange(-50, 51)
    }

    gold = location_map[request.POST['property']]
    request.session['total_gold'] += gold

    activity = {}
    if gold >= 0:
        activity['css_class'] = "won"
        activity['content'] = "Won {} gold from the {}! ({})".format(str(abs(gold)), request.POST['property'], datetime.now().strftime('%c'))
    else:
        activity['css_class'] = "lost"
        activity['content'] = "Lost {} gold from the {}! ({})".format(str(abs(gold)), request.POST['property'], datetime.now().strftime('%c'))

    request.session['activities'].append(activity)

    return redirect("/")

def destroy(request):
    request.session.clear()
    return redirect("/")