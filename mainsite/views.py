from django.shortcuts import render

def index(request):
    return render(request, 'mainsite/index.html')

def about(request):
    return render(request, 'mainsite/about.html')

def contact(request):
    return render(request, 'mainsite/contact.html')

def error_404(request):
    return render(request,'mainsite/404.html', {})

def error_500(request):
    return render(request,'mainsite/500.html', {})
