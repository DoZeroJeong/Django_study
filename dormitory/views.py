from django.shortcuts import render
from .selenium_test import dormitory_out_apply
from .models import Tu_Data
from .forms import TuDataForm

# Create your views here.


def out_apply(request):
    if request.method == 'POST':
        tu_form = TuDataForm(request.POST)

