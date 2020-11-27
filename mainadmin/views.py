from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import *
# Create your views here.

#admin Dashboard Loading

class AdminDashboard(View):
    def get(self,request):
        try:
            adminposts = ImagePosts.objects.all()
            context = {'posts':adminposts}
            return render(request,'index.html',context)
        except Exception as e:
            print(e)
    def post(self,request):
        try:
            postname = request.POST.get('postname')
            images = request.FILES
            desc = request.POST
            
            
            lend = len(images.getlist('image'))
            
            AdminPost.objects.get_or_create(post_name=postname)
            
            adminpost = AdminPost.objects.get(post_name=postname)
            for i in range(0,lend) :
                
                post = ImagePosts.objects.create(image_add=adminpost,images=images.getlist('image')[i],description=desc.getlist('desc')[i],tag=desc.getlist('tag')[i])
                
            return redirect('admindashboard')
        except Exception as e:
            print(e)

class LikedUsers(View):
    def get(self, request,id):
        post = ImagePosts.objects.get(id=id)

        statust = StatusTable.objects.filter(action=True,posts=post)

        return render(request,'likeduser.html',{'likedusers':statust})