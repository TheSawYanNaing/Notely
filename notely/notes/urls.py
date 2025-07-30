from . import views 
from django.urls import path 

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index")
]