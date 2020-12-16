from django.db import models


class Fira(models.Model):
    image = models.ImageField(upload_to='fira',)

    class Meta:
        verbose_name = "Fira"
        verbose_name_plural = "Firas"

    def __str__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('')

class Vegan(models.Model):
    id = models.IntegerField(primary_key=True)
    material = models.TextField()
    vegan = models.IntegerField()
    ovo = models.IntegerField()
    lacto = models.IntegerField()
    lactoovo = models.IntegerField()
    pesco = models.IntegerField()
    pollo = models.IntegerField()