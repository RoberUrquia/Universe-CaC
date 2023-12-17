from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def news(request):
    return render(request,"core/news.html")

def notices(request):
    return render(request,"core/notices.html")

def contact(request):
    return render(request,"core/contact.html")

def event(request):
    return render(request,"core/event.html")

def planets(request):
    return render(request,"core/planets.html")
 