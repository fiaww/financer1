from django.db import models
import uuid

class Operations_history(models.Model):

    user_UUID = models.UUIDField(default=uuid.uuid4,
                                 editable=False)
    operation_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    class Meta:
        verbose_name = ("operations_history")
        verbose_name_plural = ("operations_histories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
