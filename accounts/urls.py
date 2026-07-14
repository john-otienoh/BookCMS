from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Registration & email verification
    path("register/", views.signup_view, name="register"),
    path("register/done/", views.register_done_view, name="register_done"),
    path("register/confirm/", views.register_confirm_view, name="register_confirm"),
    path(
        "register/confirm/<uidb64>/<token>/",
        views.register_confirm_link_view,
        name="register_confirm_link",
    ),
    path("register/resend/", views.resend_otp_view, name="resend_otp"),

    # Session auth
    path("login/", views.signin_view, name="login"),
    path("logout/", views.signout_view, name="logout"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit_view, name="profile_edit"),

    # Password change / reset: 
    path("password-change/", auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change_form.html"), name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"), name="password_change_done"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

    # Google Social Auth
    # path("social-auth/", include("social_django.urls", namespace="social")),
]