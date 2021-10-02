from rest_framework import serializers
from usersignup.models import User


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", 'last_name', 'email', 'mobile_no', 'dob']
        extra_kwargs = {'first_name': {
            'error_messages': {'required': 'missed keyword first_name!', 'blank': 'first name required! '}},
            'email': {
            'error_messages': {'required': 'missed keyword email!', 'blank': 'email can not be blank!','invalid':'please enter a valid email!'}},
            'mobile_no': {
            'error_messages': {'required': 'missed keyword mobile_no!', 'blank': 'mobile number  required!','invalid':'please enter a valid mobile number!'}},
            'dob': {
            'error_messages': {'required': 'missed keyword dob!', 'blank': 'date of birth required! '}},
        }
