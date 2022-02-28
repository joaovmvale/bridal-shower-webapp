from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=255,
        default="",
        verbose_name="Nome da pessoa",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="E-mail da pessoa",
    )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def __str__(self):
        return f"{self.name}"
