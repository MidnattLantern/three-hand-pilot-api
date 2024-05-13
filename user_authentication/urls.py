from django.urls import path
from user_authentication import views

urlpatterns = [
    path('user_authentication/', views.UserAuthenticationList.as_view()),
    path('user_authentication/<int:pk>/', views.UserAuthenticationDetail.as_view()),
]