from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth import urls
from main.views import home,UserRegistration,UserProfileDetails,CustomLoginView,UserProfileUpdate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='start_journey.html'),name='start_journey_page'),
    
    path('home-page',home,name='home_page'),
    path('register/',UserRegistration.as_view(),name='registration-page'),
    path('login/', CustomLoginView.as_view(), name="login-page"),
    
    path('profile/<int:pk>',UserProfileDetails.as_view(),name='user_profile'),
    path("update/<int:pk>", UserProfileUpdate, name="user-update"),
    
    path('captcha/',include('captcha.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)