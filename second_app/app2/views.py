from django.shortcuts import render, get_object_or_404
from .models import Contact

def contacts_home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_home.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

# Create your views here.
