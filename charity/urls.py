from django.urls import path

from charity.views import *

app_name = 'charity'

urlpatterns = [
    path('add_donation/', AddDonationStep1View.as_view(), name='add_donation'),
    path('add_donation/step2/', AddDonationStep2View.as_view(), name='add_donation_step2'),
    path('add_donation/step3/', AddDonationStep3View.as_view(), name='add_donation_step3'),
    path('add_donation/step4/', AddDonationStep4View.as_view(), name='add_donation_step4'),
    path('add_donation/step5/', AddDonationStep5View.as_view(), name='add_donation_step5'),
    path('add_donation/confirmation/', ConfirmationView.as_view(), name='confirmation'),
    path('pick_up/<int:pk>/', DonationTakenView.as_view(), name='donation_taken'),
    path('donation/<int:pk>/', DonationDetailView.as_view(), name='donation_detail'),

]