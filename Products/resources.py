from import_export import resources
from .models import Product

class ProductsResources(resources.Resource):
    class Meta:
        model = Product
        fields = ('id','item_number','item_name', 'item_price')
        