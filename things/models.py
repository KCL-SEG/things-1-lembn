from django.db.models import Model, CharField, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator


class Thing(Model):
    name = CharField(blank=False, max_length=30, unique=True)
    description = CharField(blank=True, max_length=120)
    quantity = IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
