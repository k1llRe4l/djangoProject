from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Profile
from django.core.paginator import Paginator


class BlogList(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'post_detail.html'


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'


def post_count(request):
    count = Post.objects.count()
    return {'post_count': count}


def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)     # limit to 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'posts': posts})
