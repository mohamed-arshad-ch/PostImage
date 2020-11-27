from rest_framework import serializers
from mainadmin.models import AdminPost,ImagePosts,StatusTable
from django.contrib.auth.models import User

class AdminPostSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = AdminPost


class ImagePostSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField(source='image_add.post_name', read_only=True)
    post_date = serializers.DateField(source='image_add.date_created', read_only=True)
    class Meta:
        model = ImagePosts
        fields = ['post_name','post_date','images','description','tag','likes','dislikes']


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class StatusOfPost(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    posts_image = serializers.ImageField(source='posts.images', read_only=True)
    posts_likes = serializers.CharField(source='posts.likes', read_only=True)
    posts_dislikes = serializers.CharField(source='posts.dislikes', read_only=True)
    posts_tag = serializers.CharField(source='posts.tag', read_only=True)

    
    class Meta:
        model = StatusTable
        fields = ['user','posts_image','posts_tag','date_of_change','status_from_user','posts_likes','posts_dislikes']

class WhoLikedPostsIn(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = StatusTable
        fields = ['user']