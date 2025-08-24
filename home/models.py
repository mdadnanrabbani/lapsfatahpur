from django.db import models


# Create your models here.

class contactFrom(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.email}"



class Notice(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()

    to_list = models.TextField(help_text="To whom notice is addressed")
    copy_list = models.TextField(blank=True, null=True, help_text="Copy for information to")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.created_at.strftime('%d-%m-%Y')})"