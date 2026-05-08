from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mysite.urls")),
    path("users/", include("users.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
]

# Custom Error Handlers
handler400 = "mysite.views.errors.bad_request"
handler403 = "mysite.views.errors.permission_denied"
handler404 = "mysite.views.errors.page_not_found"
handler500 = "mysite.views.errors.server_error"
