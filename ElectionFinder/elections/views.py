from django.shortcuts import render

# Create your views here.

def election_form(request):
    return render(request, 'elections/index.html')

def election_result(request):
    return render(request, 'elections/result.html')