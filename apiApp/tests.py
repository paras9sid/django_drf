from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from apiApp.api import serializers
from . import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="newpassword@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix",
                                                        about="#1 platform",
                                                        website="https://www.netflix.com"
                                                        )

    def test_streamplatform_create(self):
        data={
            "name":"netflix",
            "about":"#1 ott platform",
            "website":"https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # homework - testcases for create,put and delete request for normal user - status = 403 forbidden because permission is admin/readonly in views.


class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="newpassword@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix",
                                                    about="#1 platform",
                                                    website="https://www.netflix.com"
                                                    )
        
        self.watchlist = models.Watchlist.objects.create(platform=self.stream,
                                                        title="Emaple movie",
                                                        storyline="Example story",
                                                        active=True
                                                        )

    def test_watchlist_create(self):
        data={
            "platform": self.stream,
            "title":"example movie",
            "storyline":"exmaple story",
            "active": True
        }

        response = self.client.post(reverse('watch-list'), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_watchlist_list(self):

        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_watchlist_inbd(self):
        response = self.client.get(reverse('watchlist-detail', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Watchlist.objects.count(), 1)
        self.assertEqual(models.Watchlist.objects.get().title, 'Emaple movie')


class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="newpassword@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix",
                                                    about="#1 platform",
                                                    website="https://www.netflix.com"
                                                    )
        
        self.watchlist = models.Watchlist.objects.create(platform=self.stream,
                                                        title="Emaple movie",
                                                        storyline="Example story",
                                                        active=True
                                                        )
        
        self.watchlist2 = models.Watchlist.objects.create(platform=self.stream,
                                                        title="Emaple movie",
                                                        storyline="Example story",
                                                        active=True
                                                        )
        
        self.review = models.Review.objects.create(review_user=self.user,
                                                    rating=5,
                                                    description="Greate movie!",
                                                    watchlist=self.watchlist2,
                                                    active=True)
        
    def test_review_create(self):
        data={
            "review_user": self.user,
            "rating": 5,
            "description": "Greate movie!",
            "watchlist": self.watchlist,
            "active": True,
        }

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        #get method below will show error as reviews count is more than 1
        # self.assertEqual(models.Review.objects.get().rating, 5)

        # reviewing again for the same movie - error bad req
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):

        data={
            "review_user": self.user,
            "rating": 5,
            "description": "Greate movie!",
            "watchlist": self.watchlist,
            "active": True,
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # put req
    def test_review_update(self):

        data={
            "review_user": self.user,
            "rating": 4,
            "description": "Greate movie! -updated",
            "watchlist": self.watchlist,
            "active": False,
        }

        response = self.client.put(reverse('review-detail', args=(self.review.id,)),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # create delete test case


    def test_review_user(self):
        response = self.client.get('/watch/review/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

