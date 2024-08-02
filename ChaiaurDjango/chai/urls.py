from django.urls import path
from . import views

urlpatterns = [
    path('',views.chai_home,name="chai_home"),

]