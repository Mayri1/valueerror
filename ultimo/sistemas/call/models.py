# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    vencimiento = models.DateTimeField(db_column='Vencimiento')  # Field name made lowercase.
    saldo = models.FloatField(db_column='Saldo')  # Field name made lowercase.
    comprobante = models.TextField(db_column='Comprobante')  # Field name made lowercase.
    corredor = models.TextField(db_column='Corredor')  # Field name made lowercase.
    grupo = models.TextField(db_column='Grupo')  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    mora = models.BigIntegerField(db_column='Mora')  # Field name made lowercase.
    rango_venc = models.TextField(db_column='Rango_venc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'
