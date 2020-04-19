from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'todo-detail',
        lookup_field = 'id'
    )
    class Meta:
        model = Todo
        fields = '__all__'