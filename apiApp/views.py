# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from .models import Movie


# # Create your views here.
# def movieList(request):
#     movies = Movie.objects.all()
#     # print(movies.values())
#     context = {
#         'movies': list(movies.values()),
#     }
#     # return HttpResponse('list')
#     return JsonResponse(context)
#     # return render(request,'index.html')

# def movieDetail(request,pk):
#     movie = Movie.objects.get(pk=pk)
#     print(movie)
#     context = {
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active,
#     }
#     return JsonResponse(context)
    
