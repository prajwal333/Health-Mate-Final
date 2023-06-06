from django.urls import path
from doctorapp import views

urlpatterns = [

path("drlogin/", views.drlogin, name="drlogin")

]