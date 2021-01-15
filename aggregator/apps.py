from django.apps import AppConfig


class AggregatorConfig(AppConfig):
    name = 'aggregator'

    def ready(self):
        from contentUpdater import updater
        updater.start()