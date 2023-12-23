from django.db.models import Min, F
from graphene import ObjectType, List, Schema, String, Float, Decimal
from graphene_django import DjangoObjectType

from marketapp.models import Product, Shop, ProductCategory


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'min_price', 'shop', 'product_category')


class ShopType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = '__all__'


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class CheapestProductType(ObjectType):
    product_category = String()
    shop = String()
    min_price = Float()
    name = String()


class Query(ObjectType):
    cheapest_products = List(
        CheapestProductType,
    )

    def resolve_cheapest_products(self, info):
        product_query = Product.objects.values('product_category__name', 'shop__name').annotate(min_price=Min('price'))
        result_query = []
        for item in product_query:
            result_query.append(Product.objects.filter(
                price=item['min_price'],
                shop__name=item['shop__name'],
                product_category__name=item['product_category__name'],
            ).values('product_name', 'price', 'shop__name', 'product_category__name'))
        result = []
        for query in result_query:
            for item in query:
                result.append(
                    CheapestProductType(product_category=item['product_category__name'],
                                        shop=item['shop__name'],
                                        min_price=item['price'],
                                        name=item['product_name']
                                        ))
        return result


schema = Schema(query=Query)
