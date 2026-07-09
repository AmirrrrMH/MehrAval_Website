from django.contrib import admin
from website.models import User, Success


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
