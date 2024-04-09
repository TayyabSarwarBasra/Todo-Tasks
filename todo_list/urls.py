from django.urls import path, include
from rest_framework import routers
from todo_list.views import UserSignupAPIView, CustomAuthToken, TodoList, TodoDetail, CategoryList, CategoryDetail


urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('signup', UserSignupAPIView.as_view(), name='user-signup'),
    path('api-token-auth/', CustomAuthToken.as_view()),
]