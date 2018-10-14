from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class QoldanushiProfile(models.Model):
    qoldanushi = models.OneToOneField(User, on_delete=models.CASCADE)
    sipattama = models.CharField(max_length=500,default='')
    k_b_zhumis_zh = models.CharField(max_length=100,default="Kim bolip zhumis isteisiz? Misali: Python Developer")
    qala = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    ualy_tel = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = QoldanushiProfile.objects.create(qoldanushi=kwargs['instance'])

post_save.connect(create_profile,sender=User)
