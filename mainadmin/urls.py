from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminDashboard.as_view(),name="admindashboard"),
    path('likedusers/<int:id>',LikedUsers.as_view(),name="likedusers")
]