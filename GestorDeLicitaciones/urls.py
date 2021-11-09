from django.contrib import admin
from django.urls import path
from gestorPedidos import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.views.static import serve
from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_licitaciones/',views.busqueda_licitaciones,name='busqueda'),
    path('mis_ofertas/',views.mis_ofertas,name='mis ofertas'),
    path('contacto/',views.contacto,name='contacto'),
    path('generarEvento/',views.generarEvento,name='evento'),
    path('',views.index,name='home'),
    path('documentacion/',views.documentacion,name='documentacion'),
    path('register/',views.register,name='register'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='salir'),
    path('mis_datos/',views.profile,name='mis datos'),
    path('buscarLicitaciones/',views.buscarLicitaciones),
    path('buscarMisLicitaciones/',views.buscarMisLicitaciones, name='mis_licitaciones'),
    path('modificarOferta/',views.modificarOferta,name='modificarOferta'),
    path('eliminarAnexo/',views.eliminarAnexo,name='eliminarAnexo'),
    path('upload/',views.upload_file,name="upload" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = DefaultRouter()
router.register(r'licitaciones', views.LicitacionView, basename='licitaciones')
urlpatterns += router.urls