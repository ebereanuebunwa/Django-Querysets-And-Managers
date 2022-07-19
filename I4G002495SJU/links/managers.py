from django.db import models


class ActiveLinkManager(models.Manager):
    def get_queryset(Self):
        qs = super().get_queryset()
        return qs.filter(active=True)