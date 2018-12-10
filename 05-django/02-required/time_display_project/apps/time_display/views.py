from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    print("*" * 80)
    print(context['time'])
    print("*" * 80)

    return render(request,'time_display/index.html', context)