# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ViewpointForm


# def handle_viewpoint(view_func):
#     """Decorator برای مدیریت فرم دیدگاه"""
#     def wrapper(request, *args, **kwargs):
#         if request.method == "POST":
#             form = ViewpointForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "دیدگاه شما با موفقیت ارسال شد.")
#                 return redirect(request.path)
#             else:
#                 messages.error(request, "خطا در ارسال دیدگاه. لطفاً دوباره تلاش کنید.")
#         return view_func(request, *args, **kwargs)
#     return wrapper


# @handle_viewpoint
# def article1(request):
#     form = ViewpointForm()
#     return render(request, "articles/r_t.html", {"form": form})


# @handle_viewpoint
# def article2(request):
#     form = ViewpointForm()
#     return render(request, "articles/madrese_khoob.html", {"form": form})


# @handle_viewpoint
# def article3(request):
#     form = ViewpointForm()
#     return render(request, "articles/study_konkur.html", {"form": form})


# @handle_viewpoint
# def article4(request):
#     form = ViewpointForm()
#     return render(request, "articles/summer.html", {"form": form})


# @handle_viewpoint
# def article5(request):
#     form = ViewpointForm()
#     return render(request, "articles/successـinـkonkur.html", {"form": form})


# @handle_viewpoint
# def article6(request):
#     form = ViewpointForm()
#     return render(request, "articles/social_media.html", {"form": form})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ViewpointForm


def article_page(request, template_name, page_title, redirect_name):
    """تابع حرفه‌ای برای مدیریت فرم دیدگاه در همه مقاله‌ها"""

    if request.method == "POST":
        form = ViewpointForm(request.POST)
        if form.is_valid():
            viewpoint = form.save(commit=False)
            viewpoint.article_page = page_title  # ذخیره نام صفحه
            viewpoint.save()
            messages.success(request, "✅ دیدگاه شما با موفقیت ارسال شد.")
            return redirect(redirect_name)
        else:
            messages.error(request, "❌ خطا در ارسال دیدگاه. لطفاً دوباره تلاش کنید.")
    else:
        form = ViewpointForm()

    return render(request, template_name, {"form": form})


# ویوهای هر مقاله
def article1(request):
    return article_page(
        request, "articles/r_t.html", "ریاضی و تجربی", "articles:article1"
    )


def article2(request):
    return article_page(
        request, "articles/madrese_khoob.html", "مدرسه خوب", "articles:article2"
    )


def article3(request):
    return article_page(
        request, "articles/study_konkur.html", "مطالعه کنکور", "articles:article3"
    )


def article4(request):
    return article_page(request, "articles/summer.html", "تابستان", "articles:article4")


def article5(request):
    return article_page(
        request,
        "articles/successـinـkonkur.html",
        "موفقیت در برنامه‌ریزی",
        "articles:article5",
    )


def article6(request):
    return article_page(
        request, "articles/social_media.html", "رسانه‌های اجتماعی", "articles:article6"
    )


def article7(request):
    return article_page(
        request, "articles/best_school.html", "بهترین دبیرستان", "articles:article7"
    )
