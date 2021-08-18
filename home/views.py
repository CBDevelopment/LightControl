from django.shortcuts import render

from .forms import PickForm
from django.http import HttpResponseRedirect

from .models import Effects

# Create your views here.

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PickForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PickForm()

        context = {
            'form': form,
        }
        return render(request, 'home/index.html', context)