from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validateLengthTitle(value):
    if len(value) < 3:
        raise ValidationError('Must be longer than 2 Characters')


class Note(models.Model):
    title = models.CharField(max_length=255, validators=[validateLengthTitle])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
    content = models.TextField(blank=True)
    note = models.OneToOneField(Note, related_name="desc", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)