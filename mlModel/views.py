from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def user(request):
    # username = request.GET.get('username')
    username = request.GET['username']
    return render(request, 'user.html', {'username': username})