from django.db import models

class AppointmentTime(models.Model):
    barber= models.ForeignKey("barber.Barber",on_delete=models.CASCADE,related_name="barbers")
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
      return f"Appointment time: {self.start_time} - {self.end_time}"


class Appointment(models.Model):
    STATUS=(
       (1,'Confirmed'),
       (2,'Confirmed'),
       (3,'Pending'),
       (0,'Canceled'),
    )
    customer= models.ForeignKey("customer.Customer",on_delete=models.CASCADE,related_name="appointments")
    service= models.ForeignKey("barber.Service",on_delete=models.CASCADE,related_name="appointments")
    appointment_time = models.ForeignKey(AppointmentTime,on_delete=models.CASCADE,related_name="appointments")
    status = models.IntegerField( choices=STATUS)
    note = models.TextField( max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"Appointment : {self.customer.first_name} {self.customer.last_name} {self.appointment_time.start_time} - {self.appointment_time.end_time}"
