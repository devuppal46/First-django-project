from django.urls import path
from Helloworld import views

urlpatterns=[
    path('',views.index)
]