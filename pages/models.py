from django.db import models
from django.urls import reverse

class Page(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	last_update = models.DateTimeField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('page-detail', kwargs={'page_id':self.id})


