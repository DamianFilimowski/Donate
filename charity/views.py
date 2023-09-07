from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from charity.models import *


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        bags_quantity = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        foundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        locals = Institution.objects.filter(type=3)
        context = {'bags_quantity': bags_quantity, 'foundations': foundations, 'ngos': ngos, 'locals': locals }
        return render(request, 'index.html', context)


class AddDonationStep1View(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'charity/form_step1.html', {'categories': categories})

    def post(self, request):
        categories = request.POST.getlist('categories')
        print(categories)
        return render(request, 'charity/form_step2.html', categories)




class ConfirmationView(View):
    def get(self, request):
        return render(request, 'charity/form-confirmation.html')




