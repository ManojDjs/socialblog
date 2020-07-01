from django.urls import path
from django.conf.urls import url,include
from .views import ProductList,ProductDetail
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns=[
   path('',ProductList.as_view(),name='products-list'),
    path('products/<int:pk>/',ProductDetail.as_view(),name='product-detail')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)