from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_principal_view, name='index_principal'),

]