from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='studentIndex'),
    
    #Products
    path('viewProducts', views.viewProducts, name='viewProducts'),
    path('viewProducts/<int:id>', views.viewProductsSpecific, name='viewProductsSpecific'),

    #Services
    path('viewServices', views.viewServices, name='viewServices'),
    path('viewServicesSpecific/<int:id>', views.viewServicesSpecific, name='viewServicesSpecific'),

    #Blog
    path('viewArticles', views.viewArticles, name='viewArticles'),
    path('viewArticles/<int:id>', views.viewArticle, name='viewArticle'),
]