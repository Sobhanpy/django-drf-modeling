from django.urls import path 
from .views import *

app_name = 'api-v1-accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name = 'registration'),
    path('token/login/', CustomeObtainAuthToken.as_view(), name = 'login'),
    path('token/logout/', DestroyAuthToken.as_view(), name = 'logout'),    
]