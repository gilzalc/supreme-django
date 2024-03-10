from django.shortcuts import render


# Create your views here.
def welcome_view(request, *args, **kwargs):
    print(request.user, *args, **kwargs)
    return render(request, 'pages/welcome.html', {'name': 'Zack'})
