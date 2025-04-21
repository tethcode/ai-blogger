from django.urls import path
from blogai import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogai'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('generate-blog/', views.generate_blog, name='generate-blog'),
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details'),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)