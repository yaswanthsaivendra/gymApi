from rest_framework import permissions
from gym_management_app.models import Trainer


class IsTrainerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return Trainer.objects.filter(user=request.user).exists()



class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user



class IsTrainerAndOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True 

        is_trainer = Trainer.objects.filter(user=request.user).exists()
        is_owner = obj.trainer.user == request.user

        return is_trainer and is_owner



class IsOwnerOfGymOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  

        return obj.owner == request.user
