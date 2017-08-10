from urllib.parse import quote_plus
from django.contrib import messages
# from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
from comments.models import Comment

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" : form,
    }
    return render(request, "posts/form.html", context)

def post_detail(request, slug=None):
    today = timezone.now().date()
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    share_string = quote_plus(instance.content)
    comments = Comment.objects.filter_by_instance(instance)
    context = {
        "instance" : instance,
        "title" : instance.title,
        "share_string" : share_string,
        "today":today,
        "comments":comments,
    }
    return render(request, "posts/detail.html", context)

def post_list(request):
    queryset_list = Post.objects.active()#.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "obj_list" : queryset
    }
    return render(request, "posts/postlist.html", context)
    #return HttpResponse("list")





def post_update(request ,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted ")
    return redirect("posts:list")
