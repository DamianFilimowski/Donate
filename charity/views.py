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
        return redirect('charity:add_donation_step4')


class AddDonationStep4View(View):
    def get(self, request):
        return render(request, 'charity/form_step4.html')

    def post(self, request):
        if request.POST.get('return') == 'yes':
            return redirect('charity:add_donation_step3')
        address = request.POST.get('address')
        request.session['address'] = address
        city = request.POST.get('city')
        request.session['city'] = city
        postcode = request.POST.get('postcode')
        request.session['postcode'] = postcode
        data = request.POST.get('data')
        request.session['data'] = data
        time = request.POST.get('time')
        request.session['time'] = time
        phone = request.POST.get('phone')
        request.session['phone'] = phone
        more_info = request.POST.get('more_info')
        request.session['more_info'] = more_info
        return redirect('charity:add_donation_step5')


def session_data(request):
    address = request.session.get('address')
    city = request.session.get('city')
    postcode = request.session.get('postcode')
    data = request.session.get('data')
    time = request.session.get('time')
    phone = request.session.get('phone')
    more_info = request.session.get('more_info')
    foundation = request.session.get('foundation')
    bags = request.session.get('bags')
    categories = request.session.get('categories')
    return address, city, postcode, data, time, phone, more_info, foundation, bags, categories


class AddDonationStep5View(View):
    def get(self, request):
        address, city, postcode, data, time, phone, more_info, foundation, bags, categories = session_data(request)
        context = {'address': address, 'city': city, 'postcode': postcode, 'data': data, 'time': time, 'phone': phone,
                   'more_info': more_info, 'foundation': foundation, 'bags': bags, 'categories': categories}
        return render(request, 'charity/form_step5.html', context)

    def post(self, request):
        if request.POST.get('return') == 'yes':
            return redirect('charity:add_donation_step4')
        return redirect('charity:confirmation')

class ConfirmationView(View):
    def get(self, request):
        return render(request, 'charity/form-confirmation.html')




