from django.db import models
import uuid


class Graph(models.Model):

    user_UUID = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    image = models.FileField()
    date_time = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = ("graph")
        verbose_name_plural = ("graphics")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
