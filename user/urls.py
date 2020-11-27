from django.urls import path
from .views import *


urlpatterns = [
    path('api/',ListAllPosts.as_view(),name="listallpost"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/alllikers/<int:id>',ListOfAllLikers.as_view(),name="alllikers"),
    path('api/likethepost/<int:id>/',LikeThePost.as_view(),name="likethepost"),
    path('api/dislikethepost/<int:id>/',DisLikeThePost.as_view(),name="dislikethepost"),
    path('api/wholiked/<int:id>/',WhoLikedPost.as_view(),name="wholiked"),
    

    
]
