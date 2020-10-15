from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    #check if that was a post request and if the details are valid
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()     #form.save() return the usr that just signed in to us if the form is valid 
            login(request, user)
            return redirect('article:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})   #blank form again 




def login_view(request):
    if request.method == 'POST': 
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')                    #return redirect('articles:list')
    else:                                                    #when the user type accounts/login in the url or click on the login button
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')               # change to homepage
