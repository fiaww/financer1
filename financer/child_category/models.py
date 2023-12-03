from django.db import models


class Category(models.Model):

    name = models.TextField(max_length=35)
    parent_category_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})