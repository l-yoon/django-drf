from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

@api_view(["GET"])
def product_list(request):
    cache_key = "product_list"
    
    if not cache.get(cache_key):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set("product_list", json_response, 180)
        
    json_response = cache.get(cache_key)
    return Response(json_response)
