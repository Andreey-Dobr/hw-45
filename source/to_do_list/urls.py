"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp.views import IndexView, To_Do_Create_View, Delete_To_Do, TO_Do_View, To_Do_Update_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TO_Do_View.as_view(), name='to_do_view'),
    path('to_do/add/', To_Do_Create_View.as_view(), name='to_do_create'),
    path('<int:pk>/edit/', To_Do_Update_View.as_view(), name='to_do_update'),
    path('<int:pk>/del/', Delete_To_Do.as_view(), name='del')
]
