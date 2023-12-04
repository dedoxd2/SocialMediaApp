from django.urls import path
from .views import index, signup, signin, logout, settings, upload, like_post, profile ,follow , search

urlpatterns = [
    path('', index, name='index'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('like-post', like_post, name='like-post'),
    path('profile/<str:pk>', profile, name='profile'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),

]
