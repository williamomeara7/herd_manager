from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from dateutil import parser


class Animal(models.Model):
    # class Meta:
    #     verbose_name_plural = 'animals'
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default="",
        blank=True
    )
    type = models.CharField(max_length=120)
    letter_grade = models.CharField(max_length=120)
    number_grade = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    weight = models.DecimalField(decimal_places=2, max_digits=100)

    def get_absolute_url(self):
        return reverse("animal-view", kwargs={"my_id": self.id})

    def get_all_values(self):
        query = value_per_kg.objects.filter(type=f"{self.type}", letter_grade=f"{self.letter_grade}",
                                            number_grade=f"{self.number_grade}").reverse()
        data = []
        for item in query:
            datetime_object = parser.parse(item.get_date())
            formattedDate = datetime.strftime(datetime_object, "%d/%m/%Y")
            data.append({
                "y": item.get_value_per_kg() / 100,
                "x": formattedDate
            })
        return data

    def get_all_dates(self):
        query = value_per_kg.objects.filter(type=f"{self.type}", letter_grade=f"{self.letter_grade}",
                                            number_grade=f"{self.number_grade}").reverse()
        data = []
        for item in query:
            # for it in item:

            data.append(item.get_date())
        return data

    def get_current_value(self):
        query = value_per_kg.objects.filter(type=f"{self.type}", letter_grade=f"{self.letter_grade}",
                                            number_grade=f"{self.number_grade}")
        for item in reversed(query):
            current_value = item.get_value_per_kg()
            if current_value != -1:
                return round(float(self.weight) * float(current_value / 100), 2)
            return -1

    def get_weight(self):
        return round(float(self.weight), 2)

    def get_profit(self):

        return round(self.get_current_value() - float(self.price), 2)


class value_per_kg(models.Model):
    date = models.CharField(max_length=100)
    type = models.CharField(max_length=120)
    letter_grade = models.CharField(max_length=120)
    number_grade = models.CharField(max_length=120)
    value_per_kg_cents = models.DecimalField(
        decimal_places=2, max_digits=100000)

    def get_value_per_kg(self):
        return float(self.value_per_kg_cents)

    def get_date(self):
        return self.date

# if __name__ == '__main__':
#     animal = Animal.objects.get(1)
#     animal.get_all_values()
