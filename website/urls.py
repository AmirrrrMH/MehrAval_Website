from django.urls import path
from django.views.generic import RedirectView
from website.views import (
    about,
    home,
    prerigester,
    where_x,
    successes,
    robots_txt,
    sitemap_xml,
)

app_name = "website"

urlpatterns = [
    path("", home, name="home"),
    path("prerigester/", prerigester, name="prerigester"),
    path("about/", about, name="about"),
    path("where-x/", where_x, name="where-x"),
    path("successes/", successes, name="successes"),
    path("robots.txt/", robots_txt, name="robots-txt"),
    path("sitemap.xml/", sitemap_xml, name="sitemap-xml"),

    # Redirects from old WordPress URLs
    path("about-us/", RedirectView.as_view(pattern_name="website:about", permanent=True)),
    path("contact/", RedirectView.as_view(pattern_name="website:where-x", permanent=True)),
    path("we/", RedirectView.as_view(pattern_name="website:about", permanent=True)),
    path("موفقیت-ها/", RedirectView.as_view(pattern_name="website:successes", permanent=True)),
    path("پیش-ثبت-نام/", RedirectView.as_view(pattern_name="website:prerigester", permanent=True)),
    path("پایه-ی-دهم/", RedirectView.as_view(pattern_name="website:home", permanent=True)),
    path("سوالات-متداول-مهراول/", RedirectView.as_view(pattern_name="website:home", permanent=True)),
    path("elementor-10144/", RedirectView.as_view(pattern_name="website:home", permanent=True)),
]   