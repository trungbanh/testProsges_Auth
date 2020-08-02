from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.authtoken import views as tokenViews

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path(r'api-token-auth/', tokenViews.obtain_auth_token)
]