from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.index,name='homepage'),
    path('new/', views.createRorB),
    path('roasts/', views.roast_view),
    path('boasts/', views.boast_view),
    path('mostscore/', views.sortscore),
    path('score/<int:post_id>/', views.score_view, name='score'),
    path('like/<int:post_id>/', views.like_view),
    path('dislike/<int:post_id>/', views.dislike_view)
]