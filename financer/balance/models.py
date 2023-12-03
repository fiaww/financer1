from django.db import models
import uuid


class Balance(models.Model):

    user_UUID = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    amount = models.FloatField(default = 0.00)
    class Type(models.TextChoices):
        MINUS = '-',
        PLUS = '+'

    class Meta:
        verbose_name = ("balance")
        verbose_name_plural = ("balances")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
