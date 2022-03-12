import json
from ..models import Session, Attempt, EventType, Cube


class DataExporter:
    @staticmethod
    def exportTimes():
        all_times = Attempt.objects.all().exclude(DNF=True).exclude(tags__name="Chill Solves")
        out = {'data': [a.time / 1000 for a in list(all_times)], 'labels': [a.id for a in list(all_times)]}
        return out
