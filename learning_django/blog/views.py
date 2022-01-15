from django.shortcuts import render

posts = [
    {
        'author':'fed',
        'title':'blog post',
        'content':'first!',
        'date_posted':'Jan 15, 2022',
    },
    {
        'author':'jane doe',
        'title':'blog post 2',
        'content':'second!',
        'date_posted':'Jan 16, 2022',
    }
]


def home(request):
    context = {
        'posts':posts,
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})