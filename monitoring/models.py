from django.db import models

class Election(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    evidence = models.FileField(upload_to='evidence/')
    election = models.ForeignKey(Election, on_delete=models.CASCADE)  
    date_reported = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title
