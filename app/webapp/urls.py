from django.urls import path

from webapp.views.articles import add_view, delete_view, confirm_delete#, detail_view, update_view
from webapp.views.base import IndexView
from webapp.views.articles import ArticleView, ArticleUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("articles/add/", add_view, name = 'article_add'),
    path("articles/", IndexView.as_view()),
    path("articles/<int:pk>", ArticleView.as_view(), name = 'article_detail'),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name= "article_update"),
    path("articles/<int:pk>/delete/", delete_view, name= "article_delete"),
    path("articles/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]