from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("riazi-tajrobi/", views.article1, name="article1"),
    path("madrese-khoob/", views.article2, name="article2"),
    path("konkur/", views.article3, name="article3"),
    path("summer/", views.article4, name="article4"),
    path("mofavagh-barname-rizi/", views.article5, name="article5"),
    path("social-media/", views.article6, name="article6"),
    path("best-school/", views.article7, name="article7"),
]
