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

        return render(request, 'contact.html', {'contactForm': contactForm, 'success_true': True})

    else:
        return render(request, 'contact.html', {'contactForm': contactForm})


def contact_initial(request):
    contactForm = ContactForm()
    return render(request, 'contact.html', {'contactForm': contactForm})
