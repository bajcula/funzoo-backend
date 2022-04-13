from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from accounts.viewsets import UserViewSet
from auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet



# AUTHENTICATION
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls
]
