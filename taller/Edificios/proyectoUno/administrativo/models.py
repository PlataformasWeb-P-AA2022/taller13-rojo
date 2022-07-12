from django.db import models

# Create your models here.

class Edificio(models.Model):
    tipo_edificio = (('residencial','Edificio Residencial'),('comercial','Edificio comercial'))
    nombre = models.CharField(max_length=30, unique=True)
    direccion= models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=tipo_edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_departamentos(self):
        # valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        # valor = sum(valor)  # [10.2, 20]
        valor = 0;
        for t in self.edificio_depa.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.costo_depa
        return valor

    def obtener_cantidad_cuartos(self):
        """
        """
        valor = 0;
        for t in self.edificio_depa.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo NumeroTelefonico
            valor = valor + t.num_cuartos
        return valor


class Departamento(models.Model):
    nombre = models.CharField(max_length=30)
    costo_depa = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos= models.IntegerField()

    edificio= models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="edificio_depa")

    def __str__(self):
        return "%s %d" % (self.nombre,self.num_cuartos)
