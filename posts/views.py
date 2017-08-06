from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" : form,
    }
    return render(request, "posts/form.html", context)

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
    return render(request, "posts/postlist.html", context)
    #return HttpResponse("list")

def post_update(request ,id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance" : instance,
        "title" : instance.title,
        "form" : form,
    }
    return render(request, "posts/form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted ")
    return redirect("posts:list")
