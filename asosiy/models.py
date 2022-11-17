from django.contrib.auth.models import User
from django.db import models

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    user = models.ManyToManyField(User)
    def __str__(self): return self.ism

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    qarz = models.IntegerField(default=0)
    sotuvchi  = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    def __str__(self):return f"{self.ism}, {self.nom}"


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    miqdor =models.FloatField()
    kelgan_sana = models.DateTimeField(auto_now=True)
    olchov = models.CharField(max_length=20)
    sotuvchi = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    def __str__(self):return f"{self.brend}, {self.nom}"

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    miqdor = models.FloatField()
    sana = models.DateTimeField(auto_now=True)
    sotuvchi = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    jami = models.FloatField()
    tolandi = models.FloatField()
    nasiya = models.FloatField()
    def __str__(self):return f"{self.mahsulot}, {self.mijoz}, {self.jami}"
