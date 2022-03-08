from django.db import models

# Create your models here.
from django.urls import reverse

class Animal(models.Model):
    type = models.CharField(max_length=120)
    letter_grade = models.CharField(max_length=120)
    number_grade = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=100000)
    weight = models.DecimalField(decimal_places=2, max_digits=100000)

    def get_absolute_url(self):
        return reverse("animal-view", kwargs={"my_id": self.id})

    def get_current_value(self):
        query = value_per_kg.objects.filter(type=f"{self.type}", letter_grade=f"{self.letter_grade}",
                                            number_grade=f"{self.number_grade}").reverse()
        for item in query:
            current_value = item.get_value_per_kg()
            if current_value != -1:
                return round(float(self.weight) * float(current_value / 100), 2)

    def get_profit(self):

        return round(self.get_current_value() - float(self.price), 2)


class value_per_kg(models.Model):
    date = models.CharField(max_length=100)
    type = models.CharField(max_length=120)
    letter_grade = models.CharField(max_length=120)
    number_grade = models.CharField(max_length=120)
    value_per_kg_cents = models.DecimalField(decimal_places=2, max_digits=100000)

    def get_value_per_kg(self):
        return float(self.value_per_kg_cents)

    def get_date(self):
        return self.date