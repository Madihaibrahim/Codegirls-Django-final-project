# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class Hotels(models.Model):
#     #h_id,h_name,owner ,location,rooms
#     name = models.CharField(max_length=30,default="Broomk")
#     owner = models.CharField(max_length=20)
#     location = models.CharField(max_length=50)
#     state = models.CharField(max_length=50,default="Punjab")
#     country = models.CharField(max_length=50,default="Pakistan")
#     def __str__(self):
#         return self.name


# class Rooms(models.Model):
#     ROOM_STATUS = ( 
#     ("1", "available"), 
#     ("2", "not available"),    
#     ) 

#     ROOM_TYPE = ( 
#     ("1", "regular"), 
#     ("2", "premium"),
#     ("3","deluxe"),    
#     ) 

#     #type,no_of_rooms,capacity,prices,Hotel
#     room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
#     capacity = models.IntegerField()
#     price = models.IntegerField()
#     size = models.IntegerField()
#     hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
#     status = models.CharField(choices =ROOM_STATUS,max_length = 15)
#     roomnumber = models.IntegerField()
#     def __str__(self):
#         return f"{self.hotel.name}{self.roomnumber}"

# class Reservation(models.Model):

#     check_in = models.DateField(auto_now =False)
#     check_out = models.DateField()
#     room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
#     guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
#     booking_id = models.CharField(max_length=100,default="null")
#     def __str__(self):
#         return self.guest.username
    


from django.db import models
from django.contrib.auth.models import User

# -------------------------
# Hotel Model
# -------------------------
class Hotels(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=40, default="Rooms")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="Punjab")
    country = models.CharField(max_length=50, default="Pakistan")

    def __str__(self):
        return self.name


# -------------------------
# Rooms Model
# -------------------------
class Rooms(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key

    ROOM_STATUS = ( 
        ("1", "available"), 
        ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
        ("1", "Royal"), 
        ("2", "premium"),
        ("3", "deluxe"),    
    ) 

    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    status = models.CharField(choices=ROOM_STATUS, max_length=15)
    roomnumber = models.IntegerField()

    def __str__(self):
        return f"{self.hotel.name} {self.roomnumber}"


# -------------------------
# Reservation Model
# -------------------------
class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key

    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username
