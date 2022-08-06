from django.urls import path, include

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from djoser import views as DjoserViews


urlpatterns = [ 
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/logout', DjoserViews.TokenDestroyView.as_view(), name='logout'), 
]