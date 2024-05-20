from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = "__all__"

        # tambien se pueden usar estas formas
        # fields = ['name', 'language', 'age', 'is_active']
        # fields = ('id', 'name', 'language', 'age', 'is_active')
        #
        # tambien hay otra forma de serializar
        # pero no usa modelos
        # se usa mas para serializar valores que
        # o bien provienen de diferentes fuentes
        # o son el resultado de alguna operacion
