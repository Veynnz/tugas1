from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "seller", "description", "price", "rating", "category"]
        
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_seller(self):
        seller = self.cleaned_data["seller"]
        return strip_tags(seller)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)