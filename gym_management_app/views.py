from rest_framework.generics import GenericAPIView
from gym_management_app.models import Gym, Trainer, Client, WorkoutSession
from gym_management_app.serializers import (
    GymSerializer,
    TrainerSerializer,
    ClientSerializer, 
    WorkoutSessionSerializer
)
from gym_management_app.permissions import (
   IsTrainerOrReadOnly,
   IsOwnerOrReadOnly,
   IsTrainerAndOwnerOrReadOnly,
   IsOwnerOfGymOrReadOnly
   )
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

# Gym

class GymListAPIView(
    GenericAPIView, 
    ListModelMixin,
    CreateModelMixin,
   ):

   queryset = Gym.objects.all()
   serializer_class = GymSerializer

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
      return super().perform_create(serializer)

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)


class GymDetailAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
   ):

   permission_classes = [IsOwnerOfGymOrReadOnly]
   queryset = Gym.objects.all()
   serializer_class = GymSerializer


   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

   def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

   def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)


# Trainer

class TrainerListAPIView(
    GenericAPIView, 
    ListModelMixin,
    CreateModelMixin,
   ):

   serializer_class = TrainerSerializer
   queryset = Trainer.objects.all()

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)
      return super().perform_create(serializer)

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)
   
   
class TrainerDetailAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
   ):

   serializer_class = TrainerSerializer
   permission_classes = [IsOwnerOrReadOnly]
   queryset = Trainer.objects.all()


   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

   def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

   def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)
   


# Client

class ClientListAPIView(
    GenericAPIView, 
    ListModelMixin,
    CreateModelMixin,
   ):

   serializer_class = ClientSerializer
   queryset = Client.objects.all()

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)
      return super().perform_create(serializer)

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)
   
   
class ClientDetailAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
   ):

   serializer_class = ClientSerializer
   permission_classes = [IsOwnerOrReadOnly]
   queryset = Client.objects.all()


   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

   def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

   def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)



# Workout Session

class WorkoutSessionListAPIView(
    GenericAPIView, 
    ListModelMixin,
    CreateModelMixin,
   ):

   serializer_class = WorkoutSessionSerializer
   queryset = WorkoutSession.objects.all()
   permission_classes = [IsTrainerOrReadOnly]  

   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def perform_create(self, serializer):
      trainer = Trainer.objects.filter(user=self.request.user).first()
      serializer.save(trainer=trainer)
      return super().perform_create(serializer)

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)
   
   
class WorkoutSessionDetailAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
   ):

   serializer_class = WorkoutSessionSerializer
   queryset = WorkoutSession.objects.all()
   permission_classes = [IsTrainerAndOwnerOrReadOnly]  


   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

   def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

   def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)
   
