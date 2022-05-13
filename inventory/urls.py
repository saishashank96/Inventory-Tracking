from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('insertv',views.insertv,name='insertv'),
    path('insert',views.insert,name='insert'),
    path('view',views.view,name='view'),
    path('deletev',views.deletev,name='deletev'),
    path('delete',views.delete,name='delete'),
    path('editv',views.editv,name='editv'),
    path('edit',views.edit,name='edit'),
    path('undelete',views.undelete,name='undelete'),
]
