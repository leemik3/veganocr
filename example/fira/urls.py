from django.conf.urls import url
from django.urls import path

from fira import views
from fira.views import result
from fira.views import index

urlpatterns = [


    path('', index),
    url(
        r'^create/$',
        views.FiraCreateView.as_view(),
        name='create',
    ),
    path('result/', result)
]
