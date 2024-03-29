from django.shortcuts import get_object_or_404, render
from category.models import Category

from store.models import Product

# Create your views here.
def store(request,category_slug=None):
  products=None
  cat=None
  if category_slug != None:
    cat = get_object_or_404(Category,slug=category_slug)
    products=Product.objects.filter(category=cat,is_available=True)
  else:
    products=Product.objects.all().filter(is_available=True)
  context={"products":products,"products_count":products.count()}
  return render(request,"store/store.html",context)

def product_detail(request,category_slug,product_slug):
  try:
    product = Product.objects.get(category__slug=category_slug,slug=product_slug)
  except Exception as e:
    raise e
  
  context = {'product':product}
  return render(request,"store/product_detail.html",context)
