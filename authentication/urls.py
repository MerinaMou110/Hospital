
from django.urls import path,include
from account.views import  SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView,ActivateAccountView,LogoutView,SocialLoginView

urlpatterns = [
     path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', UserLoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
     path('social-login/', SocialLoginView.as_view(), name='social_login'),  # Update this line
]