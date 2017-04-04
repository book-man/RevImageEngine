from __future__ import unicode_literals

from django.apps import AppConfig


class ImageMatchConfig(AppConfig):
    name = 'image_match'
    verbose_name = 'Image Match'

    def ready(self):
        import image_match.signals
