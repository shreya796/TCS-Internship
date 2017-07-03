
# Create your views here.
from django.shortcuts import render, redirect, render_to_response
from .forms import SLAForm,ServiceSelect
# from django.views.generic import View
# from django.contrib import messages
def service_new(request):
    if request.method == "POST":
        form = ServiceSelect(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = ServiceSelect()
    return render(request, 'sla.html', {'form': form})

def sla_new(request):
    if request.method == "POST":
        form = SLAForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = SLAForm()
    return render(request, 'sla_new.html', {'form': form})
