from django.db.models import Manager


class SurveyManager(Manager):
    def mdb(self):
        return self.using('mongodb')
