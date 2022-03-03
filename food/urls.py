from django.contrib import admin
from django.urls import path, include
from food import views

app_name = 'food'
urlpatterns = [
    path('', views.indexClassView.as_view(), name='food'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item', views.item, name='item'),
    #add items
    path('add',views.CreateItem.as_view(), name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]