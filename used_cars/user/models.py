from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.

class UserDetails(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=40)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='Zipcode')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=30)  # Field name made lowercase.

    def __str__(self):
        return self.username


fs = FileSystemStorage(location='/media/photos')


class CarDetails(models.Model):
    car_id = models.AutoField(db_column='Car_id', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE,
                                db_column='User_id')  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=20)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=20)  # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=20)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20)  # Field name made lowercase.
    photo = models.ImageField(
                              upload_to='photo', blank=True, null=True)  # Field name made lowercase.
    insurance_till = models.DateField(db_column='Insurance_Till')  # Field name made lowercase.
    kms_driven = models.IntegerField(db_column='Kms_Driven')  # Field name made lowercase.
    expected_prize = models.IntegerField(db_column='Expected_Prize')  # Field name made lowercase.
    fuel_type = models.CharField(db_column='Fuel_Type', max_length=20)

    def __str__(self):
        return f'{self.brand} {self.model}'


    # def userid(self):
    # return self.user_id.user_id
    def is_valid(self):
        pass


class EnquiryDetails(models.Model):
    e_id = models.AutoField(db_column='E_id', primary_key=True)  # Field name made lowercase.
    car_id = models.ForeignKey(CarDetails, on_delete=models.CASCADE,
                               db_column='Car_id')
    interested_user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE,
                                           db_column='Int_User_id')  # Field name made lowercase.
    message = models.IntegerField(db_column='Message', default=0)  # Field name made lowercase.

