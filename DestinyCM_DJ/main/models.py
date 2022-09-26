from django.db import models

# Create your models here.
class DestinyVendor(models.Model):
    name = models.CharField(max_length=50)
    hash = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.hash}'

class BungieAccount(models.Model):
    membershipType = models.IntegerField()
    destinyMembershipId = models.IntegerField()
    auth_token = models.IntegerField()
    
    def __str__(self):
        return f'{self.membershipType}, {self.destinyMembershipId},\n {self.auth_token}'