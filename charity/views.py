from django.shortcuts import render
from django.views import View


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity/form.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'charity/form-confirmation.html')
