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
    return HttpResponse("LOADING DETAIL...")


def post_list(request):
    """
    :return: the home page
    """
    return HttpResponse("LIST...")

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