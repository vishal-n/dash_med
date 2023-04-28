from i_18n_app.models import Article
from django.core.management.base import BaseCommand
from django.shortcuts import render
from i_18n_app.views import sync_languages_to_db

from django.dispatch import receiver
from django.core.signals import request_started


# def execute_sync_languages_view(sender, **kwargs):
#     help = "Runs "

@receiver(request_started)
class Command(BaseCommand):
    help = "Runs the sync_languages_to_db view"

    def handle(self, *args, **options):
        sync_languages_to_db()
