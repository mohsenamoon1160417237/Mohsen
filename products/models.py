from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	title = models.CharField(max_length = 255)
	body = models.TextField()
	url = models.TextField()
	pub_date = models.DateTimeField()
	icon = models.ImageField(upload_to = 'images/')
	image = models.ImageField(upload_to = 'images/')
	votes_total = models.IntegerField(default = 1)
	hunter = models.ForeignKey(User , on_delete = models.CASCADE)


	def __str__(self):
		return self.title


	def pretty_pub_date(self):
		return self.pub_date.strftime('%b %e %Y')


	def summary(self):
		if len(self.body) >= 100:
			return self.body[:100] + "..."
		else:
			return self.body
