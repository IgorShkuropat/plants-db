from django.db import models

# Create your models here.


class Company(models.Model):
    ur_lico = models.CharField('Юр. лицо', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    type = models.CharField('Тип предприятия', max_length=100, default=" ", null=True)
    ogrn = models.CharField('ОГРН', max_length=100)
    description = models.TextField('Описание', default=" ", null=True)


    def __str__(self):
        return self.ur_lico