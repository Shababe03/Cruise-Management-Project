from django.shortcuts import render

# #The is following functions are for testing only.

def sample(request):
    return render(request, 'testingapp/sample.html')
