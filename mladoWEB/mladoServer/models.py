from django.core.validators import MaxValueValidator
from django.db import models


class PersonalData(models.Model):
    name = models.CharField(max_length=20, help_text="Имя")
    surname = models.CharField(max_length=20, help_text="Фамилия")
    fatherName = models.CharField(max_length=20, help_text="Отчество")
    birthday = models.DateField()
    region = models.CharField(max_length=20, help_text="Область")
    street = models.CharField(max_length=20, help_text="Улица")
    home = models.CharField(max_length=20, help_text="Дом")
    flat = models.CharField(max_length=20, help_text="Квартира")
    phone = models.IntegerField(help_text="Номер телефона", validators=[MaxValueValidator(89999999999)])
    vk = models.CharField(max_length=11, help_text="ВК-ID")
    vk_id = models.CharField(max_length=20, help_text='непонятная хуй2ня', default='clear')
    permission = models.CharField(max_length=20, default='resident', choices=[('re', 'Резидент'),
                                                          ('re-p', 'Резидент-партнер'),
                                                          ('admin', 'Администратор'),
                                                          ('dew', 'Разработчик')
                                                          ])

    def __str__(self):
        return self.vk


class RegisterList(models.Model):
    person = models.ForeignKey(PersonalData, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
