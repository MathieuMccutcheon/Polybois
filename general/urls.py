from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index_principal_view, name='index_principal'),
    
    path('login/', LoginView.as_view(template_name='general/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]