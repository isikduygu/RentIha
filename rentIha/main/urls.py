from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='home'), #viewstaki home fonksiyonunu çalıştırır.
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('iha-create', views.iha_create, name='iha_create'),
    path('iha-list', views.iha_list, name='iha_list'),
    path('iha-list/<int:id>', views.iha_detail, name='iha_detail'),
    path('rent-iha', views.rent_create, name='rent_list'),
    path('my-iha', views.rent_detail, name='rent_detail'),
    path('rent-iha-list', views.rent_iha_list, name='rent_iha_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)