from django.contrib.auth import views
from django.urls import path
from hesab.views import ticket,dashboard,courses,contact,statusUser,response,ticker
app_name = "account"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path('dashboard/',dashboard,name='home'),
    path('contact/',contact,name='contact'),
    path('courses/',courses,name='courses'),
    path('ticket/',ticket,name='ticket'),
    path('status/',statusUser,name='status'),
    path('response',response,name='response'),
    path('ticket-datail/<int:id>',ticker,name='ticker'),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

