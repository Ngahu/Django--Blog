from django.shortcuts import render
from django.http import HttpResponse



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
   if request.user.is_authenticated():
        context = {
            "title":"REGISTERED USER List"
        }
   else:
       context = {
           "title":"List"
       }
   return render(request,"home/index.html", context)



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