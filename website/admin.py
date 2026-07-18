from django.contrib import admin
from website.models import User, Success, Teacher
from django.utils.html import format_html


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "current_field",
        "degree",
        "grade",
        "current_school",
        "field_of_study",
        "dad_phone_number",
        "student_phone_number",
        "created_date"
    )
    search_fields = ("full_name", "current_field", "current_school")
    list_filter = ("current_field", "current_school")
    ordering = ("full_name",)


@admin.register(Success)
class SuccessAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "field",
        "rank",
        "university",
    )

    list_filter = ("field",)

    search_fields = (
        "student_name",
        "rank",
        "university",
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "name",
        "subject",
        "field",
        "priority",
        "is_active",
    )

    list_display_links = (
        "image_preview",
        "name",
    )

    search_fields = (
        "name",
        "subject",
    )

    list_filter = (
        "field",
        "is_active",
    )

    list_editable = (
        "priority",
        "is_active",
    )

    ordering = (
        "priority",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    readonly_fields = (
        "image_preview_large",
    )

    fieldsets = (
        ("اطلاعات استاد", {
            "fields": (
                "image_preview_large",
                "image",
                "name",
                "slug",
                "subject",
                "field",
            )
        }),

        ("اطلاعات صفحه", {
            "fields": (
                "short_description",
                "biography",
                "experience",
            )
        }),

        ("تنظیمات", {
            "fields": (
                "priority",
                "is_active",
            )
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" style="border-radius:50%;">',
                obj.image.url,
            )
        return "-"

    image_preview.short_description = "تصویر"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="180" style="border-radius:10px;">',
                obj.image.url,
            )
        return "تصویری ثبت نشده است."

    image_preview_large.short_description = "پیش نمایش"
