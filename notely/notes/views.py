from django.shortcuts import render

# Create your views here.
# Main Page
def index(request):
    return render(request, "notes/index.html")