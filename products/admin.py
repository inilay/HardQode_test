from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from django.utils.translation import gettext_lazy as _
from .models import Profile, Product, Lesson, LessonView


class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0
    max_num = 1

class LessonViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_profile']

class UserAdmin(UserAdmin):
    inlines = (ProfileAdmin, )


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_owner']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson_name', 'lesson_duration', 'get_products']
    readonly_fields = ['get_products']

    @admin.display(description='products')
    def get_products(self, obj):
        return [product.product_name for product in obj.product_set.all()]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonView, LessonViewAdmin)
