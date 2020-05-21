from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Anime'

class Characters(models.Model):
    name = models.CharField(max_length=50)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Characters'

class Cosplays(models.Model):
    name = models.CharField(max_length=50)
    characters = models.ManyToManyField(Characters)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cosplays'
