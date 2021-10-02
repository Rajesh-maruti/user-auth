from django.test import TestCase
from usersignup.models import User

# Create your tests here.


class UserSignUP(TestCase):
    def setUp(self):
        User.objects.create(first_name="Rajesh", email="raj123@gmail.com",
                            mobile_no='9999999999', dob='2000-09-09')

    def test_user_sign_up(self):
        user = User.objects.get(mobile_no='9999999999')
        self.assertEqual(user.email, 'raj123@gmail.com')
