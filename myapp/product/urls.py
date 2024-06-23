from django.urls import path
from . import views

urlpatterns = [path('<int:product_id>', views.detail , name='detail'),
			   path('<int:product_id>/create', views.createreview , name='createreview'),
               path('review/<int:review_id>/delete',views.deletereview, name='deletereview'),
               ]
