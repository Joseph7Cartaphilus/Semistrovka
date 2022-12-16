"""PicturesSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('workshop/add/', views.create_or_edit_pin, name='add_pin'),
    path('workshop/<slug:slug_pin>/<int:id_pin>/edit/', views.create_or_edit_pin, name='edit_pin'),
    path('workshop/<slug:slug_pin>/<int:id>/', views.show_one_pin_by_slug_id, name='pin_detail_slug_id'),
    path('workshop/<slug:slug_pin>/', views.delete_pin, name='delete_pin'),
    path('gallery/', views.gallery, name='gallery'),
    path('<int:category_id>/gallery/', views.gallery, name='category'),
]
