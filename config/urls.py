# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importe as views de autenticação do Django
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imoveis/', include('imoveis.urls')),
    
    # --- Nossas Novas URLs de Autenticação ---
    # Usamos a LoginView pronta do Django, dizendo a ela qual template usar.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # A LogoutView é ainda mais simples.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('obras/', include('obras.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)