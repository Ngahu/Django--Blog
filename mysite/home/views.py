from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from . models import Post
from. forms import PostForm

def post_create(request):
    """
    :return: the form create
    """
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,

    }
    return render(request, "home/post_form.html", context)

def post_detail(request,abc=None):
    """
    :return: the detail page
    """
    instance = get_object_or_404(Post,id=abc)
    context = {
        "title": "instance.title",
        "instance":instance,
    }
    return render(request, "home/post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title":"List"
    }
    return render(request,"home/index.html",context)



def post_update(request,abc=None):
    instance = get_object_or_404(Post, id=abc)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "instance.title",
        "instance": instance,
        "form":form
    }
    return render(request,"home/post_form.html",context)







def post_delete(request):
    """
    :return: the home page
    """
    return HttpResponse("DELETE...")
