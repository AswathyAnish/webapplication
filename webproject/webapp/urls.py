from django.urls import path

from . import views
app_name='webapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>/', views.detail, name='detail'),
    path('add/', views.addtodb, name='addtodb'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
