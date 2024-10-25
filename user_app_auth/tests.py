from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


# Create your tests here.
class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username":"testcase",
            "email":"testcase@example.com",
            "password":"newpass@123",
            "password2":"newpass@123"
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # status code should match with register view response status

class LoginLogoutTestCase(APITestCase):

    #create user before login / logout test cases function
    def setUp(self):
        self.user = User.objects.create_user(username="example",
                                            password="newpassword@123"
                                            )

    def test_login(self):
        data={
            "username":"example",
            "password":"newpassword@123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' +self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
