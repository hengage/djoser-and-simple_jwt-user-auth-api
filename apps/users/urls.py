from django.urls import path, include, re_path
from django.views.generic import TemplateView
from djoser import views as DjoserViews


urlpatterns = [ 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/logout', DjoserViews.TokenDestroyView.as_view(), name='logout'), 
]

urlpatterns += [re_path('auth/activate/', TemplateView.as_view(template_name='index.html'))]