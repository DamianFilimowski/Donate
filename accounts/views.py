from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from accounts.forms import *
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
        donations = Donation.objects.filter(user=request.user, is_taken=False).order_by('-pick_up_date')
        donations_taken = Donation.objects.filter(user=request.user, is_taken=True).order_by('-pick_up_date')
        messages_received = messages.get_messages(request)
        message_list = list(messages_received)
        return render(request, 'accounts/profile.html', {'donations': donations,
                                                         'donations_taken': donations_taken, 'message_list': message_list})


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChangePasswordForm()
        messages_received = messages.get_messages(request)
        message_list = list(messages_received)
        return render(request, 'accounts/user_change_password.html', {'form': form,
                                                                      'message_list': message_list})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            new_password_confirm = form.cleaned_data['new_password_confirm']
            if request.user.check_password(old_password):
                if new_password == new_password_confirm:
                    request.user.set_password(new_password)
                    request.user.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, 'Hasło zostało zmienione.')
                    return redirect('accounts:profile')
                else:
                    messages.error(request, 'Nowe hasła nie pasują do siebie.')
            else:
                messages.error(request, 'Nieprawidłowe stare hasło.')
        return redirect('accounts:user_change_password')
