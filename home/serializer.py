from home.models import *
from rest_framework.serializers import ModelSerializer


class studentserializer(ModelSerializer):

    class Meta:
        model=student
        fields="__all__"


