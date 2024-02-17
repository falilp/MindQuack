from django.db import models
#Create your own models

class Usuarios(models.Model):
    NameUser = models.CharField(max_length=20,null=True)
    Apellidos = models.CharField(max_length=60,null=True)
    Nick = models.CharField(max_length=30,null=True)
    Email = models.CharField(max_length=50,null=True)
    FechaCreacion=models.DateTimeField(auto_now_add=True,null=True)
    #Declaracion de las variables que forman la base de datos Usuarioss
    #CharField para seleccion tipo de variable
    #null=True para que sea posible la opcion de no tener nada en la variable
    def __str__(self):
        return self.NameUser #Se utiliza para poder ver el nombre en el panel del admin
'''
Para poder hacer categorias para seleccionar seria tal que:
CATEGORY = (
            ('v1','v2'),
            ('v3','v4'),
            )
#CATEGORY Puede llamarse de otra forma
CATEGORY = models.CharField(max_length=50,null=True)
'''