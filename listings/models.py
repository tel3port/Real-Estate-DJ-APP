from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.urls import reverse
from django.template.defaultfilters import slugify


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    photo_main = models.CharField(max_length=2000)
    photo_1 = models.CharField(max_length=2000)
    photo_2 = models.CharField(max_length=2000)
    photo_3 = models.CharField(max_length=2000)
    photo_4 = models.CharField(max_length=2000)
    photo_5 = models.CharField(max_length=2000)
    photo_6 = models.CharField(max_length=2000)

    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('listing-slug', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class SiteMetaData(models.Model):
    meta_title = models.CharField(max_length=2000)
    desc1 = models.CharField(max_length=5000)
    desc2 = models.CharField(max_length=5000)
    desc3 = models.CharField(max_length=5000)
    desc4 = models.CharField(max_length=5000)
    location = models.CharField(max_length=5000)

    def __str__(self):
        return self.meta_title