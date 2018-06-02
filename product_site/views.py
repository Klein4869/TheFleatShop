from django.shortcuts import render

# Create your views here.
def product_initial(request):
    return render(request, 'product.html')

def single_initial(request):
    return render(request, 'single.html')