"""i_18n_support_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from i_18n_app.views import sync_languages_to_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include("i_18n_app.urls"))
]

def sync_languages():
    print("Sync languages in urls.py triggered")
    sync_languages_to_db()
sync_languages()

print("Called >>>>>>")
