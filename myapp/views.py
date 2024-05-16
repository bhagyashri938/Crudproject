from django.shortcuts import render,redirect
from myapp.models import Contact
from myapp.forms import ContactForm
def display(request):
    x=Contact.objects.all()
    a={
        'myappdata':x
    }
    return render(request,'display.html',a)

# Create your views here.
def add(request):
    if request.method=='POST':
            form=ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('display')
    else:
           form=ContactForm()
    b={
            'form':form
        }   
    return render(request,'add.html',b) 
            
        