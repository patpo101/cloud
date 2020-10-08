from django.shortcuts import render


def index(request):
    return render (request, 'frontend/index.html')
def about(request):
    return render (request, 'frontend/about.html')
def contact(request):
    return render (request, 'frontend/contact.html')   
def scores(request):
    return render (request, 'frontend/scores.html')           