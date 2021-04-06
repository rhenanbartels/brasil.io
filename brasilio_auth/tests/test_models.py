import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase
from model_bakery import baker

from brasilio_auth.models import NewsletterSubscriber


User = get_user_model()


class NewsletterSubscriberQuerySetTests(TestCase):
    def test_active_queryset_filter(self):
        active = baker.make(NewsletterSubscriber, user__is_active=True)
        baker.make(NewsletterSubscriber, user__is_active=False)

        active_only = NewsletterSubscriber.objects.active()
        assert 2 == NewsletterSubscriber.objects.count()
        assert active in active_only
        assert 1 == active_only.count()


class TestAvoidDuplicateEmail(TestCase):
    def test_avoid_duplicate_email(self):
        user_email = "email@example.com"
        with pytest.raises(IntegrityError):
            baker.make(User, email=user_email, _quantity=2)
