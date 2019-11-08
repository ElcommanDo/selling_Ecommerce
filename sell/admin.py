from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('available',)
    list_editable = ('available','price','stock')
    @mark_safe
    def preview(self,obj):
        return "<img src ={} width='90'/>".format(obj.image1.url)
    
    preview.allow_tags = True
    list_display = ('preview','name','price','available','stock','create_at','update_at')
    list_per_page=5

admin.site.register(Product,ProductAdmin)

