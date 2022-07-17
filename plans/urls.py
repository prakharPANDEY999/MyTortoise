from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('plans', views.all_plans, name="list-plans"),
    path('brands', views.all_plans1, name="list-plans1"),
    path('add_plan', views.add_plan, name="add-plan"),
    path('add_promotion', views.add_promotion, name="add-promotion"),
    path('add_customer_goal', views.add_customer_goal, name="add-customer_goal"),
    
]
