from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=50)
    anime = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Characters'