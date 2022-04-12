from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def revenue(request):
    return render(request,'revenue.html')

def about(request):
    return render(request,'about.html')