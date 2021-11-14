from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('category/<int:cat_id>',views.categorywise_product,name="categorywise_products"),
    path('product/<int:product_id>/<int:cat_id2>',views.fullPageDetail,name='fullPagePoductDetails')
    
]
