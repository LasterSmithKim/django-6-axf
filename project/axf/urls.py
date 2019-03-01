from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    re_path(r'^cart/$', views.cart, name='cart'),
    re_path(r'^mine/$', views.mine, name='mine'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^register/$', views.register, name='register'),


]