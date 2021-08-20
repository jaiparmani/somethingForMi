from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, "index.html", {'test':'text'})


def wrongQRCode(request):
    return render(request, "wrongQRCode.html")