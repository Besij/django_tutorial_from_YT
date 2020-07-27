from django.urls import path

from . import views

# . - из текущей директории

# Привязки на сайте:

# http://127.0.0.1:8000/articles/


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
]