from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'resumeSite/homePage.html', {})

def resumePage(request):
    return render(request, 'resumeSite/resume.html', {})

def schedulingPage(request):
    return render(request, 'resumeSite/scheduling.html', {})

def portfolioPage(request):
    return render(request, 'resumeSite/portfolio.html', {})