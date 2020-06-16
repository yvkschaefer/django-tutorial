from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
  path('snippets/', views.SnippetList.as_view()),
  path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>/', views.UserDetail.as_view()),
  path('', views.api_root),
  path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])

urlpatterns += [
  path('api-auth/', include('rest_framework.urls'))
]