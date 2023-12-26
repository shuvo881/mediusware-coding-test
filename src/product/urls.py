from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from product.views.product import CreateProductView, ProductListView
from product.views.variant import VariantView, VariantCreateView, VariantEditView, VariantDeleteView
from product.views.api_views import ProductViewSet



app_name = "product"

router = routers.DefaultRouter()
router.register('save-product', ProductViewSet, basename='')

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),
    path('variant/<int:id>/delete', VariantDeleteView.as_view(), name='delete.variant'),
    

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(), name='list.product'),
    
    #api
    path('api/',include(router.urls) )
]
