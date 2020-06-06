from django.db import models
from datetime import datetime
from django.db.models.functions import Lower

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData, showid):
        errors={}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        elif showid > 0:
            if Show.objects.filter(title__iexact=postData['title']).exclude(id=showid).exists():
                errors['title'] = "Title already exists and cannot be used for this show ID"
        elif Show.objects.filter(title__iexact=postData['title']).exists():
            errors['title'] = "Title already exists and cannot be created again"

        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters long"

        if postData['release_date'] == '':
            errors['release_date'] = "Invalid value in Release Date"
            print("Invalid value in Release Date")
        elif datetime.strptime(postData['release_date'], '%Y-%m-%d').date() > datetime.utcnow().date():
            errors['release_date'] = "Release Date must be in the past"

        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors['desc'] = "Description is optional, but must be at least 10 characters long if provided"
        # Title must be at least 2 char
        # Network must be at least 3 char
        # Release date must be in the past
        # Description is either blank or at least 10 char
        # Check if title already exists
        # Everything except description must be filled out
        # Do unique title check using ajax (including displaying errors)
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.id}) {self.title}"