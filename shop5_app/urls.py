from django.urls import path
from . import views

app_name = 'shop5_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('client/<int:client_id>/', views.client_buy, name='client_buy'),
]
