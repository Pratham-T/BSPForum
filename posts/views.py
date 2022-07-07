from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User

from .models import Post, Comment
from .forms import NewCommentForm, NewPostForm

import datetime

# Create your views here.
@login_required
def index(request):
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    latest_posts_list = Post.objects.order_by('pub_date')[:10]

    template = loader.get_template('posts/index.html')
    context = {
        'num_posts': num_posts,
        'num_users': num_users,
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'posts/index.html', context=context)


class PostView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = []
        for comment in Comment.objects.all():
            if comment.author.username == context['object'].author.username:
                comments.append(comment)
        context['comments'] = comments
        return context


@login_required()
def newPost(request):

    if request.method == 'POST':
        print(request)
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            pub_date = form.cleaned_data['pub_date']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if request.FILES:
                image = form.cleaned_data['image']
            else:
                image = None
            author = request.user
            post = Post(author = author, pub_date = pub_date, title = title, content = content, images = image)
            post.save()

            return response.HttpResponseRedirect(reverse('index'))

    else:
        proposed_return_date = datetime.datetime.now()
        form = NewPostForm(initial={'pub_date': proposed_return_date})
    
    context = {
        'form': form,
    }

    return render(request, 'posts/new_post.html', context)

@login_required
def newComment(request, pk):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            author = request.user
            post = Post.objects.get(pk=pk)
            comment = Comment(author = author, comment = content, post = post)
            comment.save()

            return response.HttpResponseRedirect(reverse('post', args=[pk]))

    else:
        form = NewCommentForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/new_comment.html', context)


def SearchResults(request):
    post_query = request.GET['post_query']
    author_query = request.GET['author_query']
    
    if post_query:
        posts = Post.objects.filter(content__icontains=post_query)
    else:
        posts = None
    
    if author_query:
        authors = User.objects.filter(last_name__icontains=author_query)\
            | User.objects.filter(first_name__icontains=author_query)\
            | User.objects.filter(username__icontains=author_query)
    else:
        authors = None
    
    context = {
        'post_search_results': posts,
        'author_search_results': authors,
    }
    return render(request, 'posts/search_results.html', context=context)