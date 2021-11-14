from django.shortcuts import render
from django.db.models import Q
from product.models import Product,ProductCategory;


def homePage(request):
    """ Home page Render Function """    
    
    # navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    # productCategories = ProductModels.ProductCategory.objects.filter(status=True)
    # products = ProductModels.Product.objects.filter(status=True).order_by('-id')[:9]
    navigationCategory=ProductCategory.objects.filter(status=True).order_by("-id")[:5]
    print(navigationCategory)
    categories = ProductCategory.objects.filter(status=True).order_by("-id")[1:]
    print(categories)

    return render(request, 'index.html',{"navigationCategory":navigationCategory,"categories":categories})
    

    # return render(request, 'index.html', {
    #     'navigationProductCategories' : navigationProductCategories,
    #     'productCategories' : productCategories,
    #     'products' : products
    # })
def categorywise_product(request,cat_id):
    categories = ProductCategory.objects.filter(status=True).order_by("-id")[0:]
    categoryWiseProducts=Product.objects.filter(product_category_id=cat_id).order_by("-id")[0:]
    
    
    return render(request,'category-products.html',{'products':categoryWiseProducts,'categories':categories})
    

def fullPageDetail(request,product_id,cat_id2):
    productFullPageDetail=Product.objects.get(id=product_id)
    product={productFullPageDetail}
  
    simmilarProducts=Product.objects.filter(product_category_id=cat_id2).filter(~Q(id=product_id)).order_by("-id")[:5]
    print(simmilarProducts)
    categories = ProductCategory.objects.filter(status=True).order_by("-id")[0:]

    return render(request,'full-product-details.html',{'product':product,'simillarProducts':simmilarProducts ,'categories':categories})




# def CategoryProducts(request, product_category_id):
#     """ Products list according to category """
#     navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
#     products = ProductModels.Product.objects.filter(product_category_id=product_category_id)
#     productCategories = ProductModels.ProductCategory.objects.filter(status=True)
#     return render(request, 'category-products.html', {
#         'navigationProductCategories' : navigationProductCategories,
#         'products' : products,
#         'productCategories':productCategories
#     })

# def ProductDetails(request, product_id):
#     navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
#     try:
#         product = ProductModels.Product.objects.get(id=product_id)
#     except ProductModels.Product.DoesNotExist:
#         product= {}
#     return render(request, 'product-details.html', {
#         'navigationProductCategories' : navigationProductCategories,
#     })