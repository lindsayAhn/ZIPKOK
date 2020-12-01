from django.db import models

# Create your models here.
from user.models import User

class Recommendation(models.Model):
    questType = models.IntegerField(default=0)
    lowaccount = models.IntegerField(default=0)
    urladress = models.CharField(max_length=1000)
    recommendationReason = models.CharField(max_length=2000)

    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

def __str__(self):
        return self.urladress


#    def __str__(self):
#        return self.user, self.urladress, self.recommendationReason

#    def __int__(self):
#        return self.lowaccount, self.questType

