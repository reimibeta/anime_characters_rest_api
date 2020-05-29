from django.db import models
import uuid 
from models.images.compress_image import compress_image
from models.randoms.random_string import random_string

class Anime(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Anime'

# character
class Characters(models.Model):
    name = models.CharField(max_length=50)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Characters'

class CharacterImages(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='photos/characters/%Y-%m-%d/thumbnails/%Y-%m-%d/', null=True, editable=False)
    image = models.ImageField(upload_to='photos/characters/%Y-%m-%d/', null=True)

    def __str__(self):
        return '' #self.image.url

    def save(self, *args, **kwargs):
        print(self.image.path)
        print(self.image.file)
        if str(self.image.path) == str(self.image.file):
            print('return true when on new file uploaded!')
        else:
            img = compress_image()
            self.thumbnail = img.image(self.image, 'thumbnail_{}'.format(uuid.uuid4().hex[:8].upper()))
            self.image.name = '{}{}'.format(random_string.ustring(), compress_image.ext(self.image))
        super(CharacterImages, self).save(*args, **kwargs)
    # def save(self):
    #     if not self.image:
    #         img = compress_image()
    #         self.thumbnail = img.image(
    #             self.image, 'thumbnail_{}'.format(uuid.uuid4().hex[:8].upper()))
    #         self.image.name = '{}{}'.format(
    #             random_string.ustring(), compress_image.ext(self.image))
    #     super(CharacterImages, self).save()

class Cosplays(models.Model):
    name = models.CharField(max_length=50)
    characters = models.ManyToManyField(Characters)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cosplays'
