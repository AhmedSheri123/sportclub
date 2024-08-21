from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='studentIndex'),
    
    #Products
    path('viewProducts', views.viewProducts, name='viewProducts'),
    path('viewProducts/<int:id>', views.viewSpecific, name='viewSpecific'),

    #Services
    path('viewServices', views.viewServices, name='viewServices'),
    path('viewServicesSpecific/<int:id>', views.viewServicesSpecific, name='viewServicesSpecific'),

    #Blog
    path('viewArticles', views.viewArticles, name='viewArticles'),
    path('viewArticle/<int:id>', views.viewArticle, name='viewArticle'),
]