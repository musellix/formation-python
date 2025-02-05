from django.http import HttpResponse
from django.shortcuts import render, redirect

import api


# Create your views here.
def redirect_dashboard(request):
    return redirect('home', days_range=30, currencies='EUR')


def dashboard(request, days_range=30, currencies="USD"):
    list_currencies = currencies.split(",")
    page_label = {7: 'semaine', 30:'mois', 365: 'année'}.get(days_range, "personnalisé")

    days, rates = api.get_rates(currencies=list_currencies, days=days_range)
    return render(request=request, template_name='devise/index.html', context={
        'rates': rates,
        'days_labels': days,
        'currencies': currencies,
        'page_label': page_label
    })