from django.db import models


class Category(models.Model):

    name = models.TextField(max_length=35)
    class Grade(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})