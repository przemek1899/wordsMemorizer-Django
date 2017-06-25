# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db import transaction

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = "create token fot users if one doesn't exist'"

    @transaction.atomic
    def handle(self, *args, **options):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
