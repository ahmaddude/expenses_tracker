from . import views
from django.urls import path,include

urlpatterns=[
    path('',views.index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),


]