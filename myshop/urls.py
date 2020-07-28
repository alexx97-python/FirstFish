from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.views import HomeView, CheckoutView
from accounts.views import logout, login, signup
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('core/', include('core.urls'), name='core'),
    path('news/', include('news.urls'), name='news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
