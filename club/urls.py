from django.urls import path

from club import views

urlpatterns = [
    path('dancers/', views.DancerList.as_view()),
    path('dancers/<int:pk>/', views.DancerDetail.as_view()),
    path('dances/', views.DanceList.as_view()),
]
