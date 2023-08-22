from django.db import models

class Schedule(models.Model):


    full_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    interview_start_time = models.TimeField()
    interview_end_time = models.TimeField()
    hr_number = models.CharField(max_length=20)
    hr_mail_id = models.EmailField()
    hr_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    round = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('ToDo', 'ToDo'),
        ('Rescheduled', 'Rescheduled'),
    ]

    DOMAIN_CHOICES = [
        ('Python', 'Python'),
        ('Data Engineering', 'Data Engineering'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    duration = models.TimeField(max_length=50, blank=True, null=True)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)



    def __str__(self):
        return f"{self.full_name} - {self.interview_start_time}"
