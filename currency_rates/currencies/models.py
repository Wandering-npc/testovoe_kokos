from django.db import models

class Currency(models.Model):
    charcode = models.CharField(max_length=3, verbose_name="Валюта",)
    date = models.DateField(verbose_name="Дата",)
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Курс",
        blank = True,
        null = True
    )

    class Meta:
        unique_together = ("charcode", "date")
        verbose_name="Курс валюты"

    def __str__(self):
        return f"{self.charcode} - {self.date}: {self.rate}"