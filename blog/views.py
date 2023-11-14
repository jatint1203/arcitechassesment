from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def create_blog(request):
    return render(request,'create_blog.html')

def update_blog(requests):
    return render(requests, 'update_blog.html')
def comment(requests):
    return render(requests, 'comment.html')

def showcomment(requests):
    return render(requests, 'show_comment.html')

