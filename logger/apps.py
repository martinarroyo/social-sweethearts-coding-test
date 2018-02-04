from django.apps import AppConfig

class LoggerConfig(AppConfig):
    name = 'logger'

    def ready(self):
        from . import signals
        super().ready()
