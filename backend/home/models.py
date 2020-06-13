from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    sfasdfasz = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="customtext_sfasdfasz",
    )
    ftghryuj5y = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_ftghryuj5y",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Ghvhggfgvcafvwse(models.Model):
    "Generated Model"
    adfvwftgbver = models.BigIntegerField()
