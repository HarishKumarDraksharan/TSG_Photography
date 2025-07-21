from django.urls import path

from photography import views

app_name = "photography"
urlpatterns = [
    path("", views.index, name="index"),
    path("contactus/", views.contactus, name= "contactus"),
]