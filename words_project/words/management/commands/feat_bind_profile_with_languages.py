# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User
from words.models import Profile


class Command(BaseCommand):
    help = "create profile fot users if one doesn't exist'"

    @transaction.atomic
    def handle(self, *args, **options):
        for user in User.objects.all():
            p = Profile.objects.get_or_create(user=user)
            # TODO assign 'SP' for each profile
