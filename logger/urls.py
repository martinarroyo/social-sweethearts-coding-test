from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('login/', views.IndexView.as_view(), name='login'),
    path('deauthorize/', csrf_exempt(views.DeauthorizeView.as_view()), name='deauthorize'),
    path('', login_required(views.ProfileView.as_view()), name='profile')
]
