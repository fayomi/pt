from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'users': users}

    return render(request, 'pt/index.html', context)

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'pt/profile.html', context)

def profile_detail(request, id):
    user = User.objects.get(id=id)
    context = {'user': user}

    return render(request, 'pt/profile_detail.html', context)



def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid:
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('profile')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request,'pt/register.html', context)
