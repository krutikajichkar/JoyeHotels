from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('hotels/', views.hotels, name='hotels'),
    path('contact/', views.contact, name='contact'),
    

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)