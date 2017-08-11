from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    title = "Login"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    context = {
        "form":form,
        "title":title,
    }
    return render(request,"accounts/acform.html",context)

def register_view(request):
    return render(request,"login_form.html",context)

def logout_view(request):
    return render(request,"login_form.html",context)
