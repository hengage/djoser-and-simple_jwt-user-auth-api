from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name']

    ordering = ["first_name"]

    fieldsets= [
        ("Basic User Details", {
            "fields": ['email', 'first_name', 'last_name',]
        }),

        (
            "User Status (sensitive area, proceed with caution)",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                ],
                "classes": ["collapse"],
            },
        ),

        (
            None,
            {
                "fields": [
                    "last_login",
                ]
            },
        ),

        (None, {"fields": ["groups", "user_permissions"]}),
    ]

    add_fieldsets = (
        (
            "User Personal Details",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),

        (
            "User status",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )