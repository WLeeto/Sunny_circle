from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=500, unique=True, verbose_name="Наименование")

    class Meta:
        verbose_name = "Работа"

    def __str__(self):
        return f'{self.name}'


class ReportType(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Тип отчета")

    class Meta:
        verbose_name = "Типы отчетов"

    def __str__(self):
        return f'{self.name}'


class Report(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название отчета")
    file = models.FileField(upload_to=None, max_length=254)
    reporttype_id = models.ForeignKey(ReportType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отчеты"

    def __str__(self):
        return f'{self.name} {self.file}'
