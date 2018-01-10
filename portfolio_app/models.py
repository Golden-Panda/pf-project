from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
import os

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=120,blank=False,null=False)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(max_length=600,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=256,null=True,blank=True)
    
    def __str__(self):
        return self.title
    def get_image_filename(self,filename):
        title = self.Portfolio.title
        slug = slugify(title)
        return "portfolio_images/%s-%s" % (slug,filename)
    
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio,default=None,related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Portfolio.objects.all().filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug,qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_portfolio_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_portfolio_receiver,sender=Portfolio)