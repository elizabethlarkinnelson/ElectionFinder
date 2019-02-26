from django.shortcuts import render

# Create your views here.

def election_form(request):
    return render(request, 'elections/index.html')