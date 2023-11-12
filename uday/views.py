from django.shortcuts import render

# Create your views here.

def silent(request):
    return render(request,'nani.html')