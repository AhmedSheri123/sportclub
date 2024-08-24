from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_dashboard_index, name="club_dashboard_index"),


    path('viewStudents', views.viewStudents, name="viewStudents"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('editStudent/<int:id>', views.editStudent, name="editStudent"),
    path('deleteStudent/<int:id>', views.deleteStudent, name="deleteStudent"),

    path('viewCoachs', views.viewCoachs, name="viewCoachs"),
    path('addCoach', views.addCoach, name="addCoach"),    
    path('editCoach/<int:id>', views.editCoach, name="editCoach"),    
    path('deleteCoach/<int:id>', views.deleteCoach, name="deleteCoach"),

    #Products

    path('addProduct', views.addProduct, name="addProduct"),
    path('editProduct/<int:id>', views.editProduct, name="editProduct"),
    path('DeleteProduct/<int:id>', views.DeleteProduct, name="DeleteProduct"),
    path('viewProducts', views.viewProducts, name="viewProducts"),

    path('addProductClassification', views.addProductClassification, name="addProductClassification"),
    path('editProductClassification/<int:id>', views.editProductClassification, name="editProductClassification"),
    path('viewProductsClassification', views.viewProductsClassification, name="viewProductsClassification"),
    path('DeleteProductsClassification/<int:id>', views.DeleteProductsClassification, name="DeleteProductsClassification"),


    #Services
    path('addServices', views.addServices, name="addServices"),
    path('editServices/<int:id>', views.editServices, name="editServices"),
    path('DeleteServices/<int:id>', views.DeleteServices, name="DeleteServices"),
    path('viewServices', views.viewServices, name="viewServices"),

    path('addServicesClassification', views.addServicesClassification, name="addServicesClassification"),
    path('editServicesClassification/<int:id>', views.editServicesClassification, name="editServicesClassification"),
    path('DeleteServicesClassification/<int:id>', views.DeleteServicesClassification, name="DeleteServicesClassification"),
    path('viewServicesClassification', views.viewServicesClassification, name="viewServicesClassification"),

    #Blog
    path('addArticle', views.addArticle, name="addArticle"),
    path('editArticle/<int:id>', views.editArticle, name="editArticle"),
    path('DeleteArticle/<int:id>', views.DeleteArticle, name="DeleteArticle"),
    path('viewArticles', views.viewArticles, name="viewArticles"),
]