from django.db import models
import datetime
import os
# Create your models here.




def get_file_path(request, filename):
    # Get the current date
    today = datetime.date.today()
    # Create a directory path based on the current date
    directory = today.strftime('%Y/%m/%d')
    # Return the full file path
    return os.path.join(directory, filename)





class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=False,blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path, height_field=None,width_field=None,max_length=None, blank=True, null=True)
    status = models.BooleanField(default=False,help_text="0 =default, 1 =hidden")
    trending = models.BooleanField(default=False,help_text="0=default 1=trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=False, blank=False)
    small_description = models.TextField(max_length=250,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, height_field=None,width_field=None,max_length=None, blank=True, null=True)
    status = models.BooleanField(default=False,help_text="0 =default, 1 =hidden")
    trending = models.BooleanField(default=False,help_text="0=default 1=trending")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)        
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']