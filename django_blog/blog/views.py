from django.shortcuts import render, redirect
from . import views
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.db.models import Q
from .models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django import forms

from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})  
@login_required
def profile_view(request): 
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})        

def posts_view(request):
    return render(request, 'blog/posts.html')

def home_view(request):
    return render(request, 'blog/base.html')


class PostListView(views.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def __str_(self):
        return self.title

class  PostDetailView(views.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def __str_(self):
        return self.title

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostCreateView(LoginRequiredMixin, views.CreateView):  
    model = Post
    form_class = PostForm
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def __str_(self):
        return self.title
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class PostUpdateView(LoginRequiredMixin, UserpassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def __str_(self):
        return self.title

class PostDeleteView(LoginRequiredMixin, UserpassesTestMixin, views.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' 
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def __str_(self):
        return self.title      

from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Comment, Post

def Post_detail_view(request, pk):
    Post = get_object_or_404(pk=pk)
    comment = Comment.objects.filter(Post=Post)
    new_comment = None
@login_required
def Commentview(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = Post
            comment.author = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {
        'form': form,
        'Post': Post
    }
    )
def CommentCreateView(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post = Post
            comment.author = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {
        'form': form,
        'Post': Post
    }
    )

def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment.html', {
        'form': form,
        'Post': comment.Post
    }
    )

@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('home')

def search_posts_view(request):
    query = request.GET.get('q', '')


    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=[query]) 
        ).distinct()

    return render(request, 'search_results.html', {'results': results, 'query': query})

from taggit.models import Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # You can create a separate template if needed
    context_object_name = 'posts'
    
    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag = Tag.objects.get(slug=tag_slug)
        return Post.objects.filter(tags__in=[tag])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs.get('tag_slug'))
        return context