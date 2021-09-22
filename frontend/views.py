from django.shortcuts import render
from product import models as ProductModels


def homePage(request):
    """ Home page Render Function """    
    print(request.GET)
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    productCategories = ProductModels.ProductCategory.objects.filter(status=True)
    products = ProductModels.Product.objects.filter(status=True).order_by('-id')[:3]

    return render(request, 'index.html', {
        'navigationProductCategories' : navigationProductCategories,
        'productCategories' : productCategories,
        'products' : products
    })


def CategoryProducts(request, product_category_id):
    """ Products list according to category """
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    products = ProductModels.Product.objects.filter(product_category_id=product_category_id)
    productCategories = ProductModels.ProductCategory.objects.filter(status=True)
    return render(request, 'category-products.html', {
        'navigationProductCategories' : navigationProductCategories,
        'products' : products,
        'productCategories':productCategories
    })

def ProductDetails(request, product_id):
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    try:
        product = ProductModels.Product.objects.get(id=product_id)
    except ProductModels.Product.DoesNotExist:
        product= {}
    return render(request, 'product-details.html', {
        'navigationProductCategories' : navigationProductCategories,
    })