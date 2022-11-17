from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import *

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"
    def validate_qarz(self,qiymat):
        if qiymat > 500000:
            raise ValidationError("Mijozda buncha qarz bolishi mumkin emas")
        return qiymat
class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"
class SotuvchiSerializer(ModelSerializer):
    class Meta:
        model = Sotuvchi
        fields = "__all__"

class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']