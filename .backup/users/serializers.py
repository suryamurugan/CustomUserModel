from rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers
from .models import aitUser
    
class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    usn = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'usn': self.validated_data.get('usn', ''),
        }

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = aitUser
        fields = ('email','name','usn')
        read_only_fields = ('email',)