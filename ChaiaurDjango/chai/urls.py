from django.urls import path
from . import views

urlpatterns = [
    path('',views.chai_home,name="chai_home"),
    path('<int:chai_id>/',views.chai_detail,name="chai_detail"),
]