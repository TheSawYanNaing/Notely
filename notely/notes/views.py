from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

from django import forms
from .models import User

import re
from validate_email import validate_email

PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\$\*\#@])[A-Za-z\d\$\*\#@]{5,8}$"
USERNAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9]{4,7}$"

# Form for registering
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=64, label="Username", widget=forms.TextInput(attrs={
        "placeholder" : "Eg. John Doe",
        "autocomplete" : "off"
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "placeholder" : "johndoe@gmail.com",
        "autocomplete" : "off"
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder" : "*****",
        "autocomplete" : "off"
    }))
    confirmPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        "placeholder" : "*****",
        "autocomplete" : "off"
    }))
    
    # For validination username
    def clean_username(self):
        username = self.cleaned_data.get("username")
        
        if not re.match(USERNAME_REGEX, username):
            raise forms.ValidationError("Username must start with a letter and be 5 to 8 characters long. Only letters and numbers are allowed.")

        return username 
    
    # For validation email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not validate_email(email):
            raise forms.ValidationError("Invalid Email")
        
        return email 
    
    # For validation password
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.match(PASSWORD_REGEX, password):
            raise forms.ValidationError("Password must be 5–8 characters long, contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character ($ * # @).")
        
        return password 
    
    # For validtion confirmPassword
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmPassword")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirmPassword", "Passwords must match")


# For for loggin in
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        "placeholder" : "johndoe@gmail.com",
        "autocomplete" : "off"
    }))
    
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "placeholder" : "*****",
        "autocomplete" : "off"
    }))
    
    # for validing email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not (validate_email(email)):
            raise forms.ValidationError("Invalid Email")
        
        return email 
    
    # for valding password
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.match(PASSWORD_REGEX, password):
            raise forms.ValidationError("Password must be 5–8 characters long, contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character ($ * # @).")

        return password
    
# Create your views here.
# Main Page
def index(request):
    return render(request, "notes/index.html")

# For Registering
def register(request):
    
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("notes:index"))
    
    if request.method == "GET":
        return render(request, "notes/register.html",{
            "form" : RegisterForm()
        })
    
    # For post method
    form = RegisterForm(request.POST)
    
    if (form.is_valid()):
        
        # Get data
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        confirmPassword = form.cleaned_data.get("confirmPassword")
        
        # try to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "notes/register.html", {
                "form" : form,
                "message" : "Email already exists"
            })
        
        # logging the user in
        login(request, user)
        
        # Redirect to home page
        return HttpResponseRedirect(reverse("notes:index"))
    
    return render(request, "notes/register.html", {
        "form" : form
    })
    
# For Logging in
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("notes:index"))
    
    if request.method == "GET":
        return render(request, "notes/login.html", {
            "form" : LoginForm()
        })
    
    # for post method
    form = LoginForm(request.POST)
    
    if form.is_valid():
        # Getting email and password
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
        user = authenticate(request, email=email, password=password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("notes:index"))
        
        return render(request, "notes/login.html", {
            "form" : form,
            "message" : "Invalid email or password"
        })
         
    return render(request, "notes/login.html", {
        "form" : form
    })

# for loggin out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("notes:register"))