from djongo import models


class SurveyManager(models.DjongoManager):
    def mdb(self):
        return self.using('mongodb')
