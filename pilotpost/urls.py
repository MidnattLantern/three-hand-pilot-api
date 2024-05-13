from django.urls import path
from pilotpost import views

urlpatterns = [
    path('pilot_post/', views.PilotPostList.as_view()),
    path('pilot_post/<int:pk>', views.PilotPostDetail.as_view()),
]