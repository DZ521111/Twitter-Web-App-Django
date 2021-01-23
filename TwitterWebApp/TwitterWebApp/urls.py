'''
Author : Dhruv B Kakadiya

'''

'''
TwitterWebApp URL Configuration

'''
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authentication_views
from Users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', users_views.register, name='register_page'),
    path('', include("Tweet.urls")),
]

# for media URLs for profile pics
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
