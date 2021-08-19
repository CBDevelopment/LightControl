from django.shortcuts import render

from .forms import PickForm
from django.http import HttpResponseRedirect

from .models import Effects, LightStrip

import os

from django.conf import settings
from pathlib import Path

import threading

# Create your views here.
def execute_effect(filename, pwm_pin, num_pixels):
    os.chdir(settings.MEDIA_ROOT / 'effects')
    # Windows
    # effect_command = f'python {filename}.py {filename} {pwm_pin} {num_pixels}'
    # Linux
    off_command = f'sudo python off.py off {pwm_pin} {num_pixels}'
    os.system(off_command)
    effect_command = f'sudo python {filename}.py {filename} {pwm_pin} {num_pixels}'
    os.system(effect_command) # add sudo?

def run_effect(strip, effect):
    strip_object = LightStrip.objects.filter(title=strip)
    if effect != None:
        effect_object = Effects.objects.filter(title=effect)[0].effect_file.path
    else:
        effect_object = Effects.objects.filter(title="Off")[0].effect_file.path
    # print(effect_object)
    # Windows
    # file_name = effect_object.split('\\')[-1].split('.')[0]
    # Linux
    file_name = effect_object.split('/')[-1].split('.')[0]
    # print(file_name)
    pwm_pin = strip_object[0].pwm_pin
    num_pixels = strip_object[0].num_pixels
    thread = threading.Thread(target=execute_effect, args=(file_name,pwm_pin,num_pixels))
    thread.start()
    for thread in threading.enumerate(): 
        print("THREAD:" + thread.name)
    

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PickForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleaned_data = form.cleaned_data
            # Run things on the Raspberry Pi
            strip = cleaned_data['which_strip']
            on_off = cleaned_data['on_off']
            effect = cleaned_data['which_effect']
            print(f'{strip} {effect}')

            run_effect(strip, effect)

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