from django.shortcuts import render


def Emlist(request):
    return render(request, 'emlist.html')

def index(request):
    return render(request, 'index.html')

# def emdelete(request):
#     return