from django.db import models

class InputData(models.Model):
    Age = models.IntegerField()
    Cholesterol = models.IntegerField()
    BP = models.IntegerField()
    Sex = models.IntegerField()
    Na_to_K = models.IntegerField()
    datestamp = models.DateTimeField()
    Result = models.IntegerField()
    # Добавьте поля для остальных признаков

    def __str__(self):
        return f"InputData: {self.Age}, {self.Cholesterol},{self.BP},{self.Sex},{self.Na_to_K}"