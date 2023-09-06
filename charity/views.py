from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from charity.models import *


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        bags_quantity = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        return render(request, 'index.html', {'bags_quantity': bags_quantity})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity/form.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'charity/form-confirmation.html')
