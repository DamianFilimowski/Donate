from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from charity.models import *
from charity.utils import filter_foundations


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
        request.session['categories'] = categories
        return redirect('charity:add_donation_step2')


class AddDonationStep2View(View):
    def get(self, request):
        return render(request, 'charity/form_step2.html')

    def post(self, request):
        if request.POST.get('return') == 'yes':
            return redirect('charity:add_donation')
        bags = request.POST.get('bags')
        request.session['bags'] = bags
        return redirect('charity:add_donation_step3')


class AddDonationStep3View(View):
    def get(self, request):
        categories = request.session.get('categories')
        foundations = filter_foundations(categories)
        if foundations:
            return render(request, 'charity/form_step3.html', {'foundations': foundations})
        return render(request, 'charity/form_step3.html',
                      {'message': 'Brak fundacji spełniającej kryteria'})

    def post(self, request):
        if request.POST.get('return') == 'yes':
            return redirect('charity:add_donation_step2')
        foundation = request.POST.get('foundation')
        print(foundation)
        request.session['foundation'] = foundation
        return redirect('charity:add_donation')



class ConfirmationView(View):
    def get(self, request):
        return render(request, 'charity/form-confirmation.html')




