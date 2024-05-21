from django.contrib import admin
from .models import Category  # Import mô hình Category

# Đăng ký mô hình Category, không phải lớp CategoryAdmin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} # Tự động điền slug dựa trên category_name
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
