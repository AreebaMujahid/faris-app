"""
Definition of urls for myapp.
"""
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.urls import path,include
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from product.forms import BootstrapAuthenticationForm  # Corrected import
from django.conf import settings
from django.conf.urls.static import static

from product import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    path('account/',include('account.urls')),
    path('product/' ,include('product.urls')), 
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls' , namespace='order')),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)