from django.shortcuts import render
from django.http import HttpResponse
from . models import Post


def post_create(request):
    """
    :return: the home page
    """

    return HttpResponse("LOADING...")

def post_detail(request):
    """
    :return: the home page
    """
    context = {
        "title": "Detail"
    }
    return render(request, "home/index.html", context)


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