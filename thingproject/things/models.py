from django.db.models import Model, CharField, IntegerField


class Thing(Model):
    name = CharField(blank=False, max_length=30)
    description = CharField(blank=True, max_length=256)
    quantity = IntegerField()
