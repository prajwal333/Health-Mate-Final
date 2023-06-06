from django.shortcuts import render

def drlogin(request):
    return render(request, 'doctorapp/login.html')
