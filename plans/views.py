from django.shortcuts import render
from .models import Plan
from .models import Promotion
from .models import CustomerGoal
from .forms import Planform
from .forms import Promotionform
from .forms import CustomerGoalform
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
  return render(request, 'home.html', {})

def all_plans(request):
  plan_list = Plan.objects.all()
  return render(request, 'plans/plans_list.html', 
         { 'plan_list': plan_list })

def all_plans1(request):
  plan_list = Plan.objects.all()
  return render(request, 'brands/sample.html', 
         { 'plan_list': plan_list })

def add_plan(request):
  submitted = False
  if request.method == "POST":
    form = Planform(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_plan?submitted=True')
  else:
    form = Planform
    if 'submitted' in request.GET:
      submitted=True
  return render(request, 'brands/add_plan.html', {'form':form, 'submitted':submitted})
  
def add_promotion(request):
  submitted = False
  if request.method == "POST":
    form = Promotionform(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_promotion?submitted=True')
  else:
    form = Promotionform
    if 'submitted' in request.GET:
      submitted=True
  return render(request, 'brands/add_promotion.html', {'form':form, 'submitted':submitted})

def add_customer_goal(request):
  submitted = False
  if request.method == "POST":
    form = CustomerGoalform(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_customer_goal?submitted=True')
  else:
    form = CustomerGoalform
    if 'submitted' in request.GET:
      submitted=True
  return render(request, 'plans/add_customer_goal.html', {'form':form, 'submitted':submitted})