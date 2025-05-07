from django.contrib import admin
from .models import CashFlowRecord, SubCategory, Category, Type, Status

class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment', 'created_at')
    list_filter = ('type', 'created_at', 'category', 'subcategory')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(CashFlowRecord, CashFlowRecordAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
