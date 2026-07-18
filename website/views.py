# ===== CODE GHABLI (comment shod) =====
# from django.shortcuts import render
# 
# 
# # Create your views here.
# def home(request):
#     return render(request, "website/index.html", {})
# ===== ENTEHAYE CODE GHABLI =====

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# from django.contrib.auth.forms import UserCreationForm
from website.forms import CreateUserForm
from django.contrib import messages
from articles.models import Article
from website.models import Success, Teacher


# Create your views here.
def home(request):
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "website/index.html", context)


def prerigester(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "با موفقیت ثبت شد")
            return redirect("website:home")
    context = {"form": form}
    return render(request, "website/preregistration.html", context)


def about(request):
    context = {}
    return render(request, "website/about.html", context)


def where_x(request):
    context = {}
    return render(request, "website/where-x.html", context)


def successes(request):

    field = request.GET.get("field")

    successes = Success.objects.all()

    if field:
        successes = successes.filter(field=field)

    context = {"successes": successes, "selected_field": field}

    return render(request, "website/successes.html", context)


def robots_txt(request):
    content = """User-agent: *
Allow: /
Sitemap: https://demo.gbfbgtdg.ir/sitemap.xml/
"""
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    urls = [
        {"loc": reverse("website:home"), "priority": "1.0", "changefreq": "weekly"},
        {"loc": reverse("website:about"), "priority": "0.9", "changefreq": "monthly"},
        {"loc": reverse("website:where-x"), "priority": "0.7", "changefreq": "monthly"},
        {"loc": reverse("website:successes"), "priority": "0.8", "changefreq": "weekly"},
        {"loc": reverse("website:prerigester"), "priority": "0.8", "changefreq": "monthly"},
    ]
    article_pages = [
        {"name": "article1", "priority": "0.6", "changefreq": "monthly"},
        {"name": "article2", "priority": "0.6", "changefreq": "monthly"},
        {"name": "article3", "priority": "0.6", "changefreq": "monthly"},
        {"name": "article4", "priority": "0.6", "changefreq": "monthly"},
        {"name": "article5", "priority": "0.6", "changefreq": "monthly"},
        {"name": "article6", "priority": "0.6", "changefreq": "monthly"},
    ]
    for a in article_pages:
        urls.append({
            "loc": reverse(f"articles:{a['name']}"),
            "priority": a["priority"],
            "changefreq": a["changefreq"],
        })

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        xml += "  <url>\n"
        xml += f"    <loc>https://demo.gbfbgtdg.ir{u['loc']}</loc>\n"
        xml += f"    <priority>{u['priority']}</priority>\n"
        xml += f"    <changefreq>{u['changefreq']}</changefreq>\n"
        xml += "  </url>\n"
    xml += "</urlset>"
    return HttpResponse(xml, content_type="application/xml")

def teachers(request):
    selected_field = request.GET.get("field")

    teachers = Teacher.objects.all()

    if selected_field:
        teachers = teachers.filter(field=selected_field)

    context = {
        "teachers": teachers,
        "selected_field": selected_field,
    }

    return render(request, "website/teachers.html", context)