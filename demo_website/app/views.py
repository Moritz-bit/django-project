from django.shortcuts import render, HttpResponse

# # Create your views here.
# def home(request):
#   return HttpResponse("Hi Juri!")

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def snake(request):
    return render(request, "snake.html",{})

def action(request):
    return render(request, "action.html",{})