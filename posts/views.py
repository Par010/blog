from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def post_create(request):
    return HttpResponse("create")

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance" : instance,
        "title" : instance.title
    }
    return render(request, "posts/detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "obj_list" : queryset
    }
    return render(request, "posts/index.html", context)
    #return HttpResponse("list")

def post_update(request):
    return HttpResponse("update")

def post_delete(request):
    return HttpResponse("delete")
