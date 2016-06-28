from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

WS_TYPE = (
	(0, 'Office'),
	(1, 'Shopping'),
	(2, 'Home'),
)

SEXT_TYPE = (
	(0, 'Male'),
	(1, 'Female')
)

class UserProfile(models.Model):
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    tel = models.CharField(max_length=50)
    sex = models.IntegerField(choices=SEXT_TYPE)

class Workplace(models.Model):
	area = models.IntegerField(default=0)
	ws_type = models.IntegerField(choices=WS_TYPE)
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=8000)
	price = models.IntegerField(default=0)
	start_date = models.DateTimeField('start of sharing')
	end_date = models.DateTimeField('end of sharing')
	register_date = models.DateTimeField('register this ws in the system')
	expire_date = models.DateTimeField('when advertising of this ws ends')
	published = models.BooleanField('is published?')
	province = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	map_location = models.CharField(max_length=200, help_text='Longitude, Latitude')
	image = models.FileField(upload_to='%Y/%m/%d/', null=True, blank=True)
	advertiser = models.ForeignKey(UserProfile)
	def active_wp(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=30)
	def __str__(self):
		return self.province + ", " + self.city

class Comment(models.Model):
	create_date = models.DateTimeField('when comment is created')
	published = models.BooleanField('is published?')
	ip = models.CharField(max_length=40)
	spam = models.BooleanField('is it spam?')
	commenter_email = models.CharField(max_length=80)
	commenter_name = models.CharField(max_length=80)
	body = models.CharField(max_length=8000)
	commenter = models.ForeignKey(UserProfile)
	workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)