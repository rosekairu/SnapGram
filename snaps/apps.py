from django.apps import AppConfig


class SnapsConfig(AppConfig):
    name = 'snaps'

def ready(self):
    import snaps.signals
