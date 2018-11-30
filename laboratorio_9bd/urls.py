from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chismes import views as chismes_views

#Router creation
router = DefaultRouter()

#Client
router.register(
	r'chismes',
	chismes_views.chismes_view_set,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    #path('api-token-auth/', obtain_jwt_token),
]

