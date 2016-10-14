from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^create/', views.create, name='create'),
    url(r'^approve/', views.approve, name='approve'),
    url(r'^join/', views.join, name='join'),
    url(r'^isavailable/', views.is_available, name='is_available'),
    url(r'^teams/', views.teams, name='teams'),
]