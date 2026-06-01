from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Med
from .forms import MedForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def dashboard(request):
    meds = Med.objects.filter(user=request.user)
    return render(request,"tracker/index.html",{"meds":meds})

@login_required
def view_med(request,med_id):
    pass

@login_required
def add_med(request):
    if request.method == "POST":
        form = MedForm(request.POST)
        if form.is_valid():
            med = form.save(commit=False)
            med.user = request.user
            med.save()
            return redirect("tracker:dashboard")

    else:
        form = MedForm()
        return render(request,"tracker/add_med.html", {"form":form})

@login_required
def edit_med(request,med_id):
    med = get_object_or_404(Med, id=med_id)
    if request.method == "POST":
        med.name = request.POST.get("name",med.name)
        med.dosage = request.POST.get("dosage",med.dosage)
        med.notes = request.POST.get("notes",med.notes)
        med.save()
    return redirect("tracker:dashboard")

@login_required
def delete_med(request, med_id):
    med = get_object_or_404(Med, id=med_id)
    if request.method == "POST":
        med.delete()
    return redirect("tracker:dashboard")

@login_required
def mark_taken(request,med_id):
    if request.method == "POST":
        med = get_object_or_404(Med,id=med_id)
        med.mark_taken()
    return redirect("tracker:dashboard")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tracker:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'reg_form': form})
