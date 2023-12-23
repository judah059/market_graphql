from django import forms

from marketapp.models import Product, ProductCategory


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields, 'blaaaaaaaaaaaaaaaaaa')
        if self.fields.get('shop'):
            ...
            # self.fields['product_category'].queryset = ProductCategory.objects.filter(
            #     shops=self.fields['shop'],
            # )
