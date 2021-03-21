from django.urls import path
import USERAPP.views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
]