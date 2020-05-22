from django.db import models
from django.db.models.signals import m2m_changed

class Topping(models.Model):
	pass

class Pizza(models.Model):
	toppings = models.ManyToManyField(Topping)

def toppings_changed(sender, **kwargs):
	print(kwargs)

m2m_changed.connect(toppings_changed, sender=Pizza.toppings.through)

p = Pizza.objects.create()
t = Topping.objects.create()
p.toppings.add(t)

