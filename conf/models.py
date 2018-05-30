from django.db import models


class Statistics(models.Model):
    sig = models.IntegerField(
        default=0
    )
    col = models.FloatField(
        default=0
    )
    rest = models.CharField(
        max_length=255
    )
    datetime_send = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = 'statistics'

    def __str__(self):
        return self.pk
