from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from club import views

urlpatterns = [
    path('dancers/', views.DancerList.as_view()),
    path('dancers/<int:pk>/', views.DancerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)