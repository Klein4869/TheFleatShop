from django.shortcuts import render

# Create your views here.

def index(request):
    if request.session['username'] != None:
        return render(request, 'index.html', {'username':request.session['username']})
    else:
        return render(request, 'index.html')