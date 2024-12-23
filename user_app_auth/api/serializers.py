from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    #overriding save method abvoe
    def save(self):
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        #password and confirm password equality check
        if password != password2:
            raise serializers.ValidationError({ 'Error': 'p1 and p2 has to be same!!'})
        
        #check email already exits in db
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({ 'Error': 'Email already exists.'})
        
        #account created manually and user info stored for registration
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account