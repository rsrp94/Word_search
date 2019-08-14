from django.core.management.base import BaseCommand
from app.models import Data


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("input")

    def handle(self, *args, **options):
        input = options["input"]
        f_obj = open(input)
        count = 0
        recs = []
        for line in f_obj:
            count += 1
            line = line.strip()
            word, occur = line.split("\t")
            recs.append(Data(word=word, count=occur))
            if count == 500:
                Data.objects.bulk_create(recs)
                recs = []
                count = 0

        f_obj.close()
