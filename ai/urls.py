"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from ai import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('mix', views.mix, name='mix'),

    path('type16', views.type16, name='type16'),
    path('EAOL', views.EAOL, name='EAOL'),
    path('IAOL', views.IAOL, name='IAOL'),
    path('IAOH', views.IAOH, name='IAOH'),
    path('EAOH', views.EAOH, name='EAOH'),
    path('ECOL', views.ECOL, name='ECOL'),
    path('ICOL', views.ICOL, name='ICOL'),
    path('ICOH', views.ICOH, name='ICOH'),
    path('ECOH', views.ECOH, name='ECOH'),
    path('ECSL', views.ECSL, name='ECSL'),
    path('ICSL', views.ICSL, name='ICSL'),
    path('ICSH', views.ICSH, name='ICSH'),
    path('ECSH', views.ECSH, name='ECSH'),
    path('EASL', views.EASL, name='EASL'),
    path('IASL', views.IASL, name='IASL'),
    path('IASH', views.IASH, name='IASH'),
    path('EASH', views.EASH, name='EASH'),
    path('NO', views.NO, name='NO'),

    path('sns', views.sns, name='sns'),

    path('isjn', views.isjn, name='isjn'),
]
