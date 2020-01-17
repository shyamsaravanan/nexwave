from django.db import models
# Create your models here.
class AccountModel(models.Model):
    user=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    class Meta:
        db_table='user_details'
    def __str__(self):
        return self.user
