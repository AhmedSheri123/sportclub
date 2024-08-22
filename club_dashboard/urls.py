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

    path('addProduct', views.addProductStock, name="addProduct"),
    path('editProductStock', views.editProductStock, name="editProductStock"),
    path('viewProductsStock', views.viewProductsStock, name="viewProductsStock"),

    path('addProductClassification', views.addProductClassification, name="addProductClassification"),
    path('editProductClassification', views.editProductClassification, name="editProductClassification"),
    path('viewProductsClassification', views.viewProductsClassification, name="viewProductsClassification"),


    #Services
    path('addServices', views.addServices, name="addServices"),
    path('editServices', views.editServices, name="editServices"),
    path('viewServices', views.viewServices, name="viewServices"),

    path('addServicesClassification', views.addServicesClassification, name="addServicesClassification"),
    path('editServicesClassification', views.editServicesClassification, name="editServicesClassification"),
    path('viewServicesClassification', views.viewServicesClassification, name="viewServicesClassification"),

    #Blog
    path('addArticle', views.addArticle, name="addArticle"),
    path('editArticle', views.editArticle, name="editArticle"),
    path('viewArticles', views.viewArticles, name="viewArticles"),
]