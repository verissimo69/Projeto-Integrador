from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=50, null=False, blank=False)
    created_at = models.DateField(verbose_name="Data de Entrega",auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)