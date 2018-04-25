from django.shortcuts import render

# Create your views here.

def index(request):
    if 'username' in  request.session:
        return render(request, 'index.html', {'username':request.session['username']})
    else:
        return render(request, 'index.html')