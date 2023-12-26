from django.views import generic
from product.models import Variant, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.TemplateView):
    template_name = "products/list.html"
    extra_context={
        'product': True
    }
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["products"] = ProductVariantPrice.objects.all() 
        return context
    
