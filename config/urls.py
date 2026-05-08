from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("projname.urls")),
    path("users/", include("users.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
]

# Custom Error Handlers
handler400 = "projname.views.errors.bad_request"
handler403 = "projname.views.errors.permission_denied"
handler404 = "projname.views.errors.page_not_found"
handler500 = "projname.views.errors.server_error"
