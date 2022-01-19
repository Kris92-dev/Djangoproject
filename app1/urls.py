from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^create$', views.create, name="create"),
    re_path(r'^view$', views.view, name="view"),
    # re_path(r'^view_text/(?P<word>[\w\-]+/)$', views.view_text, name="view_text"),
]