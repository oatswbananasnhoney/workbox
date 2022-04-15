from django.shortcuts import render, redirect
from .forms import RF
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm as AF
from .models import P
from django.contrib import messages

def update_user_data(user):
    P.objects.update_or_create(user=user,)

def r(request):
    if request.method == 'POST':
        form = RF(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.n = form.cleaned_data.get('name')
            update_user_data(user)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = RF()
    return render(request, 'a/r.html', {'form': form})

def l(request):
    if request.method == "POST":
        form = AF(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AF()
    return render(request, template_name="a/l.html", context={"login_form": form})
