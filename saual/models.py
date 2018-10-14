from django.db import models

# Create your models here.


from django.db import models


class Suraq(models.Model):
    suraq_matini = models.CharField(max_length=150)
    zhar_kun = models.DateTimeField('zharialangan kuni')
    # user = models.ForeignKey(User)
