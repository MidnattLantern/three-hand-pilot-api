from django.urls import path
from product import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
]
