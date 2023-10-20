from rest_framework import serializers
from .models import Gym, Trainer, Client, WorkoutSession


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'
        read_only_fields = ('owner',)


class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = '__all__'
        read_only_fields = ('user',)



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('user',)



class WorkoutSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutSession
        fields = '__all__'
        read_only_fields = ('trainer',)

