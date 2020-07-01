from django.db import models

# Create your models here.
class Manufracturer(models.Model):
    name=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Prodcut(models.Model):
    manufracturer=models.ForeignKey(Manufracturer,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=256)
    price=models.FloatField()
    description = models.TextField()
    image=models.ImageField(blank=True,null=True)
    shipping_cost = models.FloatField()
    quantity=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name