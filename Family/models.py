from django.db import models

class Miembro (models.Model): 
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    birth = models.DateField (auto_now_add=True, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.name}"

