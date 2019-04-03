from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Animal(models.Model):
    KIND_CHOICES = (
        ('C', 'Cat'),
        ('D', 'Dog'),
    )
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, kind {self.kind}"



