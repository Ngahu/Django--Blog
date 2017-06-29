from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import Post


def post_create(request):
    """
    :return: the home page
    """

    return HttpResponse("LOADING...")

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



def post_update(request):
    """
    :return: the home page
    """
    return HttpResponse("UPDATING...")

def post_delete(request):
    """
    :return: the home page
    """
    return HttpResponse("DELETE...")
