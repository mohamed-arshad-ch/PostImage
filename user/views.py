from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from mainadmin.models import AdminPost, ImagePosts, StatusTable
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ImagePostSerializer, UserSerializer, RegisterSerializer, StatusOfPost,WhoLikedPostsIn
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.core.mail.backends import smtp
from django.views import View
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Get All Posts


class ListAllPosts(APIView):

    def get(self, request):
        snippets = ImagePosts.objects.all()

        serializer = ImagePostSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, safe=False)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ListOfAllLikers(View):
    def get(self, request, id):
        posts = ImagePosts.objects.get(id=id)

        snippets = StatusTable.objects.filter(posts=posts)
        if snippets.exists():
            serializer = StatusOfPost(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse({"List": "List Is Not Available"}, safe=False)


class LikeThePost(APIView):
    @csrf_exempt
    def post(self, request, id):
        try:
            permission_classes = (IsAuthenticated,)
            posts = ImagePosts.objects.get(id=id)
            
            
            
            status = StatusTable.objects.get(
                user=request.user, posts=posts)
            status.status_from_user = "Liked"
            status.action = True
            status.save()
            
            statrue = StatusTable.objects.filter(action=True,posts=posts).count()
            stafalse = StatusTable.objects.filter(action=False,posts=posts).count()

            posts.likes = statrue
            posts.dislikes = stafalse
            posts.save()

            return JsonResponse({"like": "success"}, safe=False)
        except StatusTable.DoesNotExist:
            StatusTable.objects.create(user=request.user,posts=posts,status_from_user="Liked",action=True)
            posts.likes = posts.likes + 1
            posts.save()
            return JsonResponse({"Create":"Success"})


class DisLikeThePost(APIView):
    @csrf_exempt
    def post(self, request, id):
        try:
            permission_classes = (IsAuthenticated,)
            posts = ImagePosts.objects.get(id=id)

            
            print(request.user)
            status = StatusTable.objects.get(
                user=request.user, posts=posts)
            
            status.status_from_user = "Dislike"
            status.action = False
            status.save()

            statrue = StatusTable.objects.filter(action=True,posts=posts).count()
            stafalse = StatusTable.objects.filter(action=False,posts=posts).count()

            posts.likes = statrue
            posts.dislikes = stafalse
            posts.save()
            
            
            


            return JsonResponse({"dislike": "success"}, safe=False)
        except StatusTable.DoesNotExist:
            StatusTable.objects.create(user=request.user,posts=posts,status_from_user="DisLiked",action=False)
            posts.dislikes = posts.dislikes + 1
            posts.save()
            return JsonResponse({"Create":"Success"})

class WhoLikedPost(APIView):
    def get(self,request,id):
        imagepost = ImagePosts.objects.get(id=id)

        statuspost = StatusTable.objects.filter(posts=imagepost,action=True)
        serializer = WhoLikedPostsIn(statuspost, many=True)
        return JsonResponse(serializer.data, safe=False)