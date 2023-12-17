from django.shortcuts import render
from .models import project

# Create your views here.
def gallery(request):
    projects = project.objects.all()
    return render(request,"gallery/gallery.html", {'projects':projects})