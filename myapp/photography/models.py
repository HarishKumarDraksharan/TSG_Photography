from django.db import models

# Create your models here.

class Section1Slideshow(models.Model):
    image = models.ImageField(upload_to='images/section1/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Section1 Slide {self.order}: {self.image.name}"
    
class Section2OurExpertise(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   

from django.db import models

class Section3Background(models.Model):
    background_image = models.ImageField(upload_to='section3_backgrounds/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)  # Dynamic title
    subtitle = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Section 3 Background"
