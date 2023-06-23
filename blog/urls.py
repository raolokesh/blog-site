from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page , name="start-page"),
    path("posts", views.post_page , name= "posts-page"),
    path("posts/<slug:slug>", views.single_post , name = "single-post"),
    

]