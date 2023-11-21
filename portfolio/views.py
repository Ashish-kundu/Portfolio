from django.shortcuts import render,HttpResponse
from datetime import datetime
from portfolio.models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("this is ur home page")

def about(request):
    return render(request, "about.html")

def achievement(request):
    return render(request, "achievement.html")

def project(request):
    return render(request, "project.html")

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contacts=Contact(name=name,address=address,email=email,phone=phone,date=datetime.today())
        contacts.save()
    return render(request, "contact.html")
    # return HttpResponse("this is ur Contact page")
