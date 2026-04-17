from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse


# ✅ Home route
def home(request):
    return JsonResponse({"message": "Backend is running 🚀"})


urlpatterns = [
    # Home
    path('', home),

    # Admin panel
    path('admin/', admin.site.urls),

    # App routes
    path('api/', include('prompts.urls')),

    # 🔐 JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]