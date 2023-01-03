from django.urls import path
from . import views

urlpatterns = [
    path('lokale', views.local_list, name='local_list'),
    path('local_form/<str:pk>', views.local_form, name='local_form'),
    path('dodaj_lokal', views.local_add, name='local_add'),
    path('local_delete/<str:pk>', views.local_delete, name='local_delete'),
    path('lokal/<str:pk>', views.local, name='local'),

    path('product_list', views.product_list, name='product_list'),
    path('product_add', views.product_add, name='product_add'),
    path('product_edit/<str:pk>', views.product_edit, name='product_edit'),
    path('product_delete/<str:pk>', views.product_delete, name='product_delete'),
    
    path('rating_list', views.rating_list, name='rating_list'),
    path('rating_add/<str:pk>', views.rating_add, name='rating_add'),
    path('rating_edit/<str:pk>', views.rating_edit, name='rating_edit'),
    path('rating_delete/<str:pk>', views.rating_delete, name='rating_delete'),
]