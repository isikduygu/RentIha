from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Iha(models.Model):
    brand= models.CharField(max_length=100)
    model = models.CharField(max_length= 100)
    weight = models.CharField(max_length= 100)
    category= models.CharField(max_length= 100)

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.weight + ' ' + self.category
    
# Iha kiralamak için model oluşturuldu. Veritabanların ilişkisi bu kısımda yapıldı. 
# user ve iha veritabanının foreignkey'si rent veritabanına bağlandı. onetoMany ilişkisi one user many rent
class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    
    def __str__(self):
        return self.user + ' ' + self.iha + ' ' + self.start_date + ' ' + self.end_date