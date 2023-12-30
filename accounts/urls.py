from django.urls import path
from accounts.views import login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]