from django.contrib import admin
from .models import Product

from django.utils.safestring import mark_safe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'quantidade', 'esta_ativo', 'imagem')

    def nome(self, obj):
        return obj.name

    def descricao(self, obj):
        return obj.description

    def preco(self, obj):
        return obj.price

    def quantidade(self, obj):
        return obj.quantity

    def esta_ativo(self, obj):
        return obj.is_active

    def imagem(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image.url))
         
    search_fields = ('name', 'description', 'price', 'quantity', 'is_active')
