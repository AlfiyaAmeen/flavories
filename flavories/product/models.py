from django.db import models

# Create your models here.
class fruits(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    qty=models.IntegerField()
    desc=models.TextField()
    date=models.DatetimeField(auto_now_add=True)
