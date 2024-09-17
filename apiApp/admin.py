from django.contrib import admin
# from .models import Movie
from .models import Watchlist, StreamPlatform, Review


# Register your models here.
# admin.site.register(Movie)
admin.site.register(Watchlist)
admin.site.register(StreamPlatform)
admin.site.register(Review)