from django.conf.urls import url

from . views import (
    post_list,
    post_create,
    post_update,
    post_detail,
    post_delete,
)

urlpatterns = [
    url(r'^$',post_list),
    url(r'^create/$',post_create),
    url(r'^(?P<abc>\d+)$',post_detail, name='detail'), #detail
    url(r'^(?P<abc>\d+)/edit/$',post_update,name='update'),
    url(r'^delete/$',post_delete),

]
