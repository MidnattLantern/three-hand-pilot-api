from django.urls import path
from serial_number import views

urlpatterns = [
    path('serial_number/', views.SerialNumberList.as_view()),
    path('serial_number/<int:pk>', views.SerialNumberDetail.as_view()),
]