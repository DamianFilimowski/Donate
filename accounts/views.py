from django.shortcuts import render, redirect
from django.views import View

from accounts.models import CustomUser


# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        last_name = request.POST.get('surname')
        first_name = request.POST.get('name')
        if password1 == password2 and not CustomUser.objects.filter(email=email):
            CustomUser.objects.create(password=password1, email=email, last_name=last_name, first_name=first_name)
            return redirect('accounts:login')
        else:
            return redirect('accounts:register')


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
