from django import forms
from accounts.models import StudentProfile, CoachProfile
from students.models import Blog, ServicesModel, ProductsClassificationModel, ServicesClassificationModel, ProductsModel

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'phone', 'birthday']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'اسم الكامل', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'phone': forms.TextInput(attrs={'placeholder':'رقم الهاتف', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'birthday': forms.DateInput(attrs={'type':'date', 'placeholder':'تاريخ الميلاد', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }

class CoachProfileForm(forms.ModelForm):

    class Meta:
        model = CoachProfile
        fields = ['full_name', 'phone', 'stadium']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'اسم الكامل', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'phone': forms.TextInput(attrs={'placeholder':'رقم الهاتف', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'stadium': forms.DateInput(attrs={'placeholder':'الملعب', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }

class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'desc', 'img', 'body']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'desc': forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'img': forms.FileInput(attrs={'accept':"image/*", 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'body': forms.Textarea(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }


class ServicesModelForm(forms.ModelForm):

    class Meta:
        model = ServicesModel
        fields = ['title','desc','age_from','age_to', 'price', 'classification', 'is_enabled']

        widgets = {
        'title': forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'desc': forms.Textarea(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'age_from': forms.NumberInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'age_to': forms.NumberInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'price':forms.NumberInput(attrs={'step': 0.00, 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'classification':forms.SelectMultiple(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'is_enabled':forms.CheckboxInput(),
        }

class ServicesClassificationModelForm(forms.ModelForm):

    class Meta:
        model = ServicesClassificationModel
        fields = ['title']

        widgets = {
            'title':forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'})
        }




class ProductsModelForm(forms.ModelForm):

    class Meta:
        model = ProductsModel
        fields = ['title','desc', 'price', 'stock', 'classification', 'is_enabled']

        widgets = {
        'title': forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'desc': forms.Textarea(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'price':forms.NumberInput(attrs={'step': 0.00, 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'stock':forms.NumberInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'classification':forms.SelectMultiple(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        'is_enabled':forms.CheckboxInput(),
        }

class ProductsClassificationModelForm(forms.ModelForm):

    class Meta:
        model = ProductsClassificationModel
        fields = ['title']

        widgets = {
            'title':forms.TextInput(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'})
        }
