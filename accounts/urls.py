from django.contrib.auth.views import LoginView
from django.urls.conf import include,path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]