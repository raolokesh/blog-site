from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hike-in-mountains",
        "image": "mountains.jpg",
        "author": "Lokesh Rao",
        "date": date(2022,6,23),
        'title': "mountain-hiking",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur quis voluptatibus, reprehenderit provident id omnis quam recusandae repellat magni, consectetur soluta fuga iure, obcaecati sequi eveniet nesciunt aut necessitatibus! Libero.",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt aperiam sequi nam vel earum minus consequatur et ad excepturi facilis nostrum, optio iusto nulla at dignissimos esse, ab dolor obcaecati!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab ex qui soluta quisquam laborum consectetur modi assumenda, doloremque obcaecati dolores nisi reprehenderit natus et laudantium illo, eius odio delectus ipsam"""
    },
        {
        "slug": "hike-in-mountains",
        "image": "woods.jpg",
        "author": "Lokesh Rao",
        "date": date(2022,6,22),
        'title': "mountain-hiking",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur quis voluptatibus, reprehenderit provident id omnis quam recusandae repellat magni, consectetur soluta fuga iure, obcaecati sequi eveniet nesciunt aut necessitatibus! Libero.",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt aperiam sequi nam vel earum minus consequatur et ad excepturi facilis nostrum, optio iusto nulla at dignissimos esse, ab dolor obcaecati!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab ex qui soluta quisquam laborum consectetur modi assumenda, doloremque obcaecati dolores nisi reprehenderit natus et laudantium illo, eius odio delectus ipsam"""
    },
        {
        "slug": "hike-in-mountains",
        "image": "mountains.jpg",
        "author": "Lokesh Rao",
        "date": date(2022,6,25),
        'title': "mountain-hiking",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur quis voluptatibus, reprehenderit provident id omnis quam recusandae repellat magni, consectetur soluta fuga iure, obcaecati sequi eveniet nesciunt aut necessitatibus! Libero.",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt aperiam sequi nam vel earum minus consequatur et ad excepturi facilis nostrum, optio iusto nulla at dignissimos esse, ab dolor obcaecati!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab ex qui soluta quisquam laborum consectetur modi assumenda, doloremque obcaecati dolores nisi reprehenderit natus et laudantium illo, eius odio delectus ipsam"""
    },
        {
        "slug": "hike-in-mountains",
        "image": "mountains.jpg",
        "author": "Lokesh Rao",
        "date": date(2022,6,20),
        'title': "mountain-hiking",
        "excerpt": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur quis voluptatibus, reprehenderit provident id omnis quam recusandae repellat magni, consectetur soluta fuga iure, obcaecati sequi eveniet nesciunt aut necessitatibus! Libero.",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt aperiam sequi nam vel earum minus consequatur et ad excepturi facilis nostrum, optio iusto nulla at dignissimos esse, ab dolor obcaecati!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab ex qui soluta quisquam laborum consectetur modi assumenda, doloremque obcaecati dolores nisi reprehenderit natus et laudantium illo, eius odio delectus ipsam"""
    },
]

def get_date(posts):
    return posts["date"]
# Create your views here.

def starting_page(request):
    sorted_post = sorted(all_posts , key=get_date)
    latest_post = sorted_post[-3:]
    return render(request , "blog/index.html", {
        "posts" : latest_post,

        
    })

def post_page(request):
    sorted_post = sorted(all_posts , key=get_date)
    return render(request , "blog/all_posts.html",
    {
        "all_posts":sorted_post,

    })

def  single_post(request,slug):
    post_details = next(post for post in all_posts if post["slug"]== slug)
    return render(request , "blog/post_details.html",
    {
        "posts": post_details,
    })