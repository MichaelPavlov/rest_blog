"""djblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^login/', login_view, name="login"),
    url(r'^register/', register_view, name="register"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^', include("posts.urls", namespace='posts')),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/posts/', include("posts.api.urls", namespace='posts-api')),
    url(r'^api/comments/', include("comments.api.urls", namespace='comments-api')),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1pcmFrIiwiZW1haWwiOiJidWRkYWhAaW5ib3gucnUiLCJ1c2VyX2lkIjoxLCJleHAiOjE0NjI4MjgyNTZ9.x8mC1caUDeh93f3v-QU-H-khbbTfQY3bJKRZ0wjX03M"}



curl -X POST -d "username=mirak&password=Andro259" http://127.0.0.1:8000/api/auth/token/


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pcmFrIiwiZW1haWwiOiJidWRkYWhAaW5ib3gucnUiLCJleHAiOjE0NjI5NTg2NzAsInVzZXJfaWQiOjF9.BCdIevTSxEj825Om-PDQM9K-hQOdQGywSb7qvUpSxf4" -H "Content-Type: application/json" -d '{"content":"New commanet trough api call"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-post&type=post'

"""
