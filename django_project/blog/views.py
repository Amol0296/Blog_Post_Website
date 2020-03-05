from django.shortcuts import render

posts = [
    {
        'author':'Amol',
        'title':'Blog Post 1',
        'content':'First post content',
        'posted_on':'3rd march 2020'
    },
    {
        'author':'Sasuke',
        'title':'Blog Post 2',
        'content':'Second post content',
        'posted_on':'3rd march 2020'
    },
    {
        'author':'Luffy',
        'title':'Blog Post 3',
        'content':'Third post content',
        'posted_on':'3rd march 2020'
    }
]


def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context,{'title':'Home'})


def about(request):
    return render(request,'blog/about.html',{'title':'About'})

