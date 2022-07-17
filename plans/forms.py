from django import forms
from django.forms import ModelForm

from .models import Plan
from .models import Promotion
from .models import CustomerGoal

class Planform(ModelForm):
  class Meta:
    model = Plan
    fields= "__all__"

class Promotionform(ModelForm):
  class Meta:
    model = Promotion
    fields = "__all__"

class CustomerGoalform(ModelForm):
  class Meta:
    model = CustomerGoal
    fields = {"user", "plans"}