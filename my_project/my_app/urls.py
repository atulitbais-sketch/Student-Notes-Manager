from django.urls import path

from . import views

urlpatterns = [
    path('na/', views.home, name='home'),
    path('na/',views.name,name="abc")
]

