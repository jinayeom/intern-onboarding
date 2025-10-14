from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path("modules/", views.modules_index, name="modules"), 
    path("modules/<slug:slug>/", views.module_detail, name="module-detail"),
]