from django.db import models
import uuid


class User(models.Model):

    UUID = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    join_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})