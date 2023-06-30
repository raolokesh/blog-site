from django.shortcuts import render
from datetime import date
from .models import Post
from django.shortcuts import get_object_or_404




# def get_date(posts):
#     return posts["date"]
# Create your views here.

def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    # sorted_post = sorted(all_posts , key=get_date)
    # latest_post = sorted_post[-3:]
    return render(request , "blog/index.html", {
        "posts" : latest_post,

        
    })

def post_page(request):
    sorted_post = Post.objects.all().order_by("-date")
    # sorted_post = sorted(all_posts , key=get_date)
    return render(request , "blog/all_posts.html",
    {
        "all_posts":sorted_post,

    })

def  single_post(request,slug):
    # post_details = Post.objects.get(slug = slug )
    post_details = get_object_or_404(Post,slug = slug )
    # post_details = next(post for post in all_posts if post["slug"]== slug)
    return render(request , "blog/post_details.html",
    {
        "posts": post_details,
        "posts_tag": post_details.tag.all()
    })

