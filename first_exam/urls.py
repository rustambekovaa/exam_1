"""
URL configuration for first_exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from first_exam import settings
from django.contrib import admin
from django.urls import path, include  
from workspace import views as workspace_views
from moobile import views as moobile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', workspace_views.login_profile, name='login'),
    path('auth/logout/', workspace_views.logout_profile, name='logout'),
    path('auth/register/', workspace_views.register, name='register'),
    path('auth/change-profile/', workspace_views.change_profile, name='change_profile'),
    path('auth/change-password/', workspace_views.change_password, name='change_password'),
    path('workspace/',include('workspace.urls')),   
    path('', include('moobile.urls')),
    path('', moobile_views.index, name='index')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
