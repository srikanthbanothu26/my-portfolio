from django.shortcuts import render
from Resume.models import Detail

def overview(request):
    details=Detail.objects.all()
    return render(request,"index.html",{"details": details })


def education(request):
    details=Detail.objects.all()
    return render(request, "education.html",{"details": details })




def Skills(request):
    details=Detail.objects.all()
    return render(request, "skills.html",{"details": details })





def Projects(request):
    details=Detail.objects.all()
    return render(request, "projects.html",{"details": details })




def Uiapplications(request):
    details=Detail.objects.all()
    return render(request, "uiapplications.html",{"details": details })


def Workexperience(request):
    details=Detail.objects.all()
    return render(request, "work_experience.html",{"details": details })


def Contact(request):
    details=Detail.objects.all()
    return render(request, "Contact.html",{"details": details })



