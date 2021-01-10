from django.urls import path
from .views import (
    # post_list, 
    # post_detail, 
    # post_create, 
    # post_update, 
    # post_delete,
    # BasedViewUrl
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDelete)

app_name = 'blog'

urlpatterns = [
    # path('', post_list, name = 'post_list'),
    # path('<slug:get_slug>/', post_detail, name = 'post_detail'),
    # path('update/<slug:get_slug>/', post_update, name = 'post_update'),
    # path('delete/<slug:get_slug>/', post_delete, name = 'post_delete'),
    # path('new/create/', post_create, name = 'post_create'),

    # BasedView
    path('', PostListView.as_view(), name = 'post_list'),
    path('<slug:get_slug>/', PostDetailView.as_view(), name = 'post_detail'),
    path('update/<slug:get_slug>/', PostUpdateView.as_view(), name = 'post_update'),
    path('delete/<slug:get_slug>/', PostDelete.as_view(), name = 'post_delete'),
    path('new/create/', PostCreateView.as_view(), name = 'post_create'),


    

]