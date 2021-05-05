from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_cntent = models.TextField()
    tutorial_published = models.DateTimeField("Date Published")
    def __str__(self):
        return self.tutorial_title
    