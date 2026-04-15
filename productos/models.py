from django.db import models


from django.db import models

class Alfajor(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    relleno = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
