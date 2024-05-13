from django.urls import path
from address_book import views

urlpatterns = [
    path('address_book/', views.AddressList.as_view()),
    path('address_book/<int:pk>', views.AddressDetail.as_view()),
]
