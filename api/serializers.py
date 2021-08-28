from rest_framework import serializers
from rest_framework.exceptions import server_error
from todo.models import ToDo

class ToDoSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  description = serializers.CharField(max_length=150)
  completed = serializers.BooleanField()

  def create(self, validated_data):
    return ToDo.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
      instance.description = validated_data.get('description', instance.description)
      instance.completed = validated_data.get('completed', instance.completed)
      instance.save()
      return instance