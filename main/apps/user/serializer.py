# from .models import User
# from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



# class UserRegistrationSerializer(serializers.ModelSerializer):   
#     confirm_password = serializers.CharField(
#         write_only = True,
#         required = True,
#         help_text = 'Enter confirm password',
#         style = {'input_type': 'password'}
#     )

#     class Meta:
#         model = User
#         fields = (
#             "first_name",
#             "last_name",
#             'phone_number',
#             'password',
#             'confirm_password'
#         )    

#     def create(self, validated_data):
#         if validated_data.get('password') != validated_data.get('confirm_password'):
#             raise serializers.ValidationError({"message":"Password and confirm password don't match"}) 
#         validated_data.pop('confirm_password') 
#         auth_user = User.objects.create_user(**validated_data)
#         return auth_user


# class UserLoginSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)

#         data['id'] = self.user.id
#         data['guid'] = self.user.guid
#         data['first_name'] = self.user.first_name
#         data['last_name'] = self.user.last_name
#         return data
    


# class UserDetailSerializer(serializers.ModelSerializer):
#     balance = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=True)
#     profile_pic = serializers.CharField(source='profile_pic.profile_picture.url')
#     default_image_guid = serializers.CharField(source='profile_pic.guid')
#     created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "guid",
#             "first_name",
#             "last_name",
#             "phone_number",
#             "profile_pic",
#             "default_image_guid",
#             "is_active",
#             "balance",
#             'created_at'
#         )


from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username'
        )


class UserRegistrationSerializer(serializers.ModelSerializer):   
    confirm_password = serializers.CharField(
        write_only = True,
        required = True,
        help_text = 'Enter confirm password',
        style = {'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            "username",
            'password',
            'confirm_password'
        )    

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError({"message":"Password and confirm password don't match"}) 
        validated_data.pop('confirm_password') 
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['username'] = self.user.username
        return data