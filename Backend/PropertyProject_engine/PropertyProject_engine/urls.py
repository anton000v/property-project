from django.contrib import admin
# from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

# urlpatterns = i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('',include('PropertyProject_api.urls')),
#     prefix_default_language=False
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('PropertyProject_api.urls')),
]
