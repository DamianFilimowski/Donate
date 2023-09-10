from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import AddUserModelForm
from accounts.models import CustomUser
from charity.models import Donation


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = AddUserModelForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = AddUserModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('accounts:login')
        return redirect('accounts:register')


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('LandingPage')
        return redirect('accounts:register')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('LandingPage')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        donations = Donation.objects.filter(user=request.user)
        return render(request, 'accounts/profile.html', {'donations': donations})