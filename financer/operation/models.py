from django.db import models


class Operation(models.Model):

    category_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    amount = models.FloatField(default = 0.00)
    date_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Type(models.TextChoices):
        MINUS = '-',
        PLUS = '+'

    class Meta:
        verbose_name = ("operation")
        verbose_name_plural = ("operations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
