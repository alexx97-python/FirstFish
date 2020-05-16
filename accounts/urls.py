from django.urls import path
from .views import logout, login, signup


app_name = 'accounts'

#urlpatterns = [
#    path('login/', login, name='login'),
#    path('logout/', logout, name='logout'),
#    path('signup', signup, name='signup'),
#]