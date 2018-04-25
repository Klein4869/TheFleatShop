from django.shortcuts import render

from .forms import ContactForm

from .models import contact_info


# Create your views here.

def contact(request):
    contactForm = ContactForm()
    if request.method == 'GET':
        username = request.GET.get('username', None)
        email = request.GET.get('email', None)
        content = request.GET.get('content', None)

        Contact_Info = contact_info.objects.create(username=username, email=email, content=content)
        ContactForm.save()

        if request.session['username'] != None:
            return render(request, 'contact.html', {'contactForm': contactForm, 'success_true': True, 'username':request.session['username']})
        else:
            return render(request, 'contact.html', {'contactForm': contactForm, 'success_true': True,})

    else:
        if request.session['username'] != None:
            return render(request, 'contact.html', {'contactForm': contactForm, 'username':request.session['username']})
        else:
            return render(request, 'contact.html', {'contactForm': contactForm,})


def contact_initial(request):
    contactForm = ContactForm()
    if request.session['username'] != None:
        return render(request, 'contact.html', {'contactForm': contactForm, 'username':request.session['username']})
    else:
        return render(request, 'contact.html', {'contactForm':contactForm})