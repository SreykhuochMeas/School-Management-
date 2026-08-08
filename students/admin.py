from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    # Show ID, name, email, score, and active status in the list view
    list_display = ('id', 'name', 'email', 'score', 'is_active')
    
    # Add search functionality by name and email
    search_fields = ('name', 'email')
    
    # Add a filter sidebar by active status
    list_filter = ('is_active',)
    
    # Challenge: Add ordering by newest record first (using created_at or id)
    ordering = ('-created_at',)
    
    # Challenge: Make certain fields read-only in the admin form
    readonly_fields = ('created_at', 'updated_at')

# Register the model with the customized configuration
admin.site.register(Student, StudentAdmin)