from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login/', views.IndexView.as_view(), name='login'),
    path('deactivate/', views.DeactivateView.as_view(), name='deactivate'),
    path('', login_required(views.ProfileView.as_view()), name='profile')

]
