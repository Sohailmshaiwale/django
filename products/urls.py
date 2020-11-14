from django.urls import path
from . import views # . represents the current folder import views does work but there can be overlapping

urlpatterns = [
    path('', views.index),# we are not calling this function django will do that for us when the url is activated
    path('new',views.new) # whatever we add in the quotes we have to add it in the url 
]