"""meusite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import IndexView, ListProjectView
import environ

environ.Env.read_env()
env = environ.Env()

urlpatterns = [
    path(env('ADMIN'), admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/project/', ListProjectView.as_view(), name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

