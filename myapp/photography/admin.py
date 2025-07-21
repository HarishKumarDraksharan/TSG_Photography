from django.contrib import admin
from .models import Section2OurExpertise, Section1Slideshow, Section3Background


# Register your models here.

class PostService(admin.ModelAdmin):
    list_display =('title', 'description')
    search_fields =('title', 'description')
    list_filter =('title', 'created_at' )

admin.site.register(Section1Slideshow)
admin.site.register(Section2OurExpertise)
admin.site.register(Section3Background)



