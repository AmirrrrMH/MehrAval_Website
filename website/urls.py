# ===== CODE GHABLI (comment shod) =====
# from django.urls import path
# from .views import home
# 
# app_name = "website"
# 
# urlpatterns = [
#     path("", home, name="home"),
# ]
# ===== ENTEHAYE CODE GHABLI =====

from django.urls import path
from website.views import about, home, prerigester, where_x, successes, robots_txt, sitemap_xml

app_name = "website"

urlpatterns = [
    path("", home, name="home"),
    path("prerigester/", prerigester, name="prerigester"),
    path("about/", about, name="about"),
    path("where-x/", where_x, name="where-x"),
    path("successes/", successes, name="successes"),
    path("robots.txt/", robots_txt, name="robots-txt"),
    path("sitemap.xml/", sitemap_xml, name="sitemap-xml"),
]
