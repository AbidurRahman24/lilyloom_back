from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router = DefaultRouter() 

router.register('list', views.SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('user/', views.profile, name='user'),
    # path('api/get_all_logged_in_users/', views.get_all_logged_in_users, name='get_all_logged_in_users'),
]