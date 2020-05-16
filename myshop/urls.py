from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.views import HomeView, CheckoutView
from accounts.views import logout, login, signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('core/', include('core.urls'), name='core'),
]
