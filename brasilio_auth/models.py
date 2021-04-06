from django.contrib.auth.models import User
from django.db import models


User._meta.get_field("email")._unique = True


class NewsletterSubscriberQuerySet(models.QuerySet):
    def active(self):
        return self.filter(user__is_active=True)


class NewsletterSubscriber(models.Model):
    objects = NewsletterSubscriberQuerySet.as_manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
