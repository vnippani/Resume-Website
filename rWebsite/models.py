from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	image = models.ImageField(upload_to='rWebsite/images/') 
	full_info = models.TextField()
	

	def __str__(self):
		return self.title #makes each item visible in admin page.