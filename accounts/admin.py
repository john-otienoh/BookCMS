from django.contrib import admin

from .models import EmailOTP, Profile


@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "purpose", "code", "is_used", "created_at", "expires_at")
    list_filter = ("purpose", "is_used")
    search_fields = ("user__username", "user__email", "code", "token")
    readonly_fields = ("code", "token", "created_at")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "updated_at")
    search_fields = ("user__username", "user__email")