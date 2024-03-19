from django.contrib import admin

from .models import Category,Product,Tag,ProductAttribute,ProductImage
from django.utils.safestring import mark_safe


class ProductAttributeStackedInline(admin.StackedInline):
    model = ProductAttribute
    extra = 1



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','id')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','category','date')
    list_display_links = ('id','title',)
    search_fields = ('title','content','category')
    list_filter = ('is_published','date')
    filter_horizontal = ('tags',)
    raw_id_fields = ('category',)
    inlines = (ProductAttributeStackedInline,)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)



    # @admin.display(description='Изображение')
    # def get_image(self, news: ProductImage):
    #     return mark_safe(f'<img src="{ProductImage.image.url}" width="150px">')

    # @admin.display(description='Изображение')
    # def get_full_image(self, news: ProductImage):
    #     return mark_safe(f'<img src="{ProductImage.image.url}" width="50%">')


# Register your models here.
