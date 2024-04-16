from django.contrib import admin

from .models import Category, Product, Tag, ProductAttribute, ProductImage
from django.utils.safestring import mark_safe


class ProductAttributeStackedInline(admin.StackedInline):
    model = ProductAttribute
    extra = 1


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 1




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','id')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','category','date','get_image')
    list_display_links = ('id','title',)
    search_fields = ('title','content','category')
    list_filter = ('is_published','date')
    filter_horizontal = ('tags',)
    raw_id_fields = ('category',)
    # readonly_fields = ('date','get_full_image')
    inlines = (ProductAttributeStackedInline, ProductImageStackedInline)


    @admin.display(description='Изображение')
    def get_image(self, product: Product):
        if product.images.first() :
            if product.images.first().image: 
                return mark_safe(f'<img src="{product.images.first().image.url}" width="100px">')

    # @admin.display(description='Изображение')
    # def get_full_image(self, product: Product):
    #     return mark_safe(f'<img src="{product.images.url}" width="50%">')



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('id',)
#     list_display_links = ('id',)



    # @admin.display(description='Изображение')
    # def get_image(self, news: ProductImage):
    #     return mark_safe(f'<img src="{ProductImage.image.url}" width="150px">')

    # @admin.display(description='Изображение')
    # def get_full_image(self, news: ProductImage):
    #     return mark_safe(f'<img src="{ProductImage.image.url}" width="50%">')


# Register your models here.
