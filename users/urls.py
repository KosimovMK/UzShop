from users.views import login, register
from django.urls import path, include

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
