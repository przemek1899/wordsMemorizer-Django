# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from words.models import Language
from words.constants import LANGUAGES


class Command(BaseCommand):
    help = 'load basic languages'

    def handle(self, *args, **options):
        for key, name in LANGUAGES:
            Language.objects.get_or_create(name=key)



