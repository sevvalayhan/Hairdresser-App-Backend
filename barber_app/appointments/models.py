from django.db import models
from datetime import datetime,timedelta


class AppointmentDetail(models.Model):
    barber = models.ForeignKey("barber.Barber", on_delete=models.CASCADE, related_name="barbers")
    service = models.ForeignKey("barber.Service", on_delete=models.CASCADE, related_name="appointments")
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True,)

    def save(self, *args, **kwargs): 
        if self.service and self.start_time:
            start_datetime = datetime.combine(datetime.today(), self.start_time)
            service_duration = timedelta(minutes=self.service.duration)
            end_datetime = start_datetime + service_duration
            self.end_time = end_datetime.time()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment Detail: {self.start_time} - {self.end_time}"
 

class Appointment(models.Model):
    STATUS=(
       (1,'Confirmed'),       
       (2,'Pending'),
       (3,'Rejected'),
       (0,'Canceled'),
    )
    customer= models.ForeignKey("customer.Customer",on_delete=models.CASCADE,related_name="appointments")
    appointment_detail = models.ForeignKey(AppointmentDetail,on_delete=models.CASCADE,related_name="appointments")
    status = models.IntegerField( choices=STATUS)
    note = models.TextField( max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"Appointment : {self.customer.first_name} {self.customer.last_name} {self.appointment_detail.start_time} - {self.appointment_detail.end_time}"
