from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book #Import Book model from models

# Register your models here.

#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author') # Filter books by title and author
    search_fields = ('title', 'author')
                     
admin.site.register(Book, BookAdmin)

#Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('email', 'is_staff', 'date_of_birth', 'username', 'profile_photo')
admin.site.register(CustomUser, CustomUserAdmin)

