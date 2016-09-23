from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^create/', views.create, name='create'),
    url(r'^join/', views.join, name='join'),
]