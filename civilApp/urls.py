
# civilApp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from casos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")), 

    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #urls casos
    path('casos/',views.casos, name = "casos"),#url de casos
    path('casos/expedientes/',views.expedientes, name = "expedientes"), #url de expedientes
    path('casos/expedientes/vista',views.vista, name = "vista_casos"),
    path('casos/eliminar/<int:id>',views.eliminar_caso, name = "eliminar_caso"),
    path('casos/expedientes/vista_expediente',views.vista_expediente, name = "vista_expediente"),
    path('casos/eliminar_expediente/<int:id>',views.eliminar_expediente, name = "eliminar_expediente"),

    # Incluye las URLs de tu nueva aplicación
    path("expedientes/", include("visualizacion_expedientes.urls")), # <--- Añade esta línea

]

# Servir archivos subidos en DEV
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
