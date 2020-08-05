from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

# from rest_framework.authtoken import views as tokenViews

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += [
    # path(r'api-token-auth/', tokenViews.obtain_auth_token)
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]