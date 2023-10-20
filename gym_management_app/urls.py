from django.urls import path
from .views import (
   GymListAPIView, GymDetailAPIView,
   TrainerListAPIView, TrainerDetailAPIView,
   ClientListAPIView, ClientDetailAPIView,
   WorkoutSessionListAPIView, WorkoutSessionDetailAPIView
)

app_name = 'gym_management_app'

urlpatterns = [
   path('gyms/', GymListAPIView.as_view(), name='gym-list'),
   path('gyms/<int:pk>/', GymDetailAPIView.as_view(), name='gym-detail'),
   path('trainers/', TrainerListAPIView.as_view(), name='trainer-list'),
   path('trainers/<int:pk>/', TrainerDetailAPIView.as_view(), name='trainer-detail'),
   path('clients/', ClientListAPIView.as_view(), name='client-list'),
   path('clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),
   path('workouts/', WorkoutSessionListAPIView.as_view(), name='workout-list'),
   path('workouts/<int:pk>/', WorkoutSessionDetailAPIView.as_view(), name='workout-detail'),
]
