from django.urls import path
from django.views.generic import ListView
from .views import BlogList, BlogDetailView, AboutPageView, ProfileView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', BlogList.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]
