from django.urls import path
from . import views

# URL CONF MODULE
urlpatterns = [
    path('', views.Homepage),
]
