from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# AUTH VIEWS
from django.contrib.auth import views as auth_views

urlpatterns = [

    # =========================================
    # ADMIN
    # =========================================

    path('admin/', admin.site.urls),

    # =========================================
    # AUTHENTICATION
    # =========================================

    path(
        '',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # =========================================
    # DASHBOARD
    # =========================================

    path('dashboard/', include('dashboard.urls')),

    # =========================================
    # MODULES
    # =========================================

    path('expenses/', include('expenses.urls')),

    path('sales/', include('sales.urls')),

    path('inventory/', include('inventory.urls')),

    path('staff/', include('staff.urls')),

    path('management-funds/', include('management_funds.urls')),

]

# =========================================
# MEDIA FILES
# =========================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )