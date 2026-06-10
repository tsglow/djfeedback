from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user_name", "rating")
    def __str__(self):
        return f'{self.user_name}, {self.rating}'
    
admin.site.register(Review,ReviewAdmin)