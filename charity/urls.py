from django.urls import path

from charity.views import *

app_name = 'charity'

urlpatterns = [
    path('add_donation/', AddDonationView.as_view(), name='add_donation'),
    path('add_donation/confirmation/', ConfirmationView.as_view(), name='confirmation'),

]