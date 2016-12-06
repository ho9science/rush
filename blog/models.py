from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Bronze(models.Model):
	class Meta:
		db_table = 'goldrodger'
	code = models.CharField(primary_key=True, max_length=6)
	sales = models.IntegerField()
	businessprofits = models.IntegerField()
	continuing = models.IntegerField()
	netincome = models.IntegerField()
	netincomeruling = models.IntegerField()
	netincomenon = models.IntegerField()
	asset = models.IntegerField()
	liabilities = models.IntegerField()
	totalequities = models.IntegerField()
	totalequitiesruling = models.IntegerField()
	totalequitiesnon = models.IntegerField()
	eqities = models.IntegerField()
	cashbusiness = models.IntegerField()
	cashinvestment = models.IntegerField()
	cashfinance = models.IntegerField()
	capex = models.FloatField()
	fcf = models.FloatField()
	ibl = models.FloatField()
	roop = models.FloatField()
	netprofitmargin = models.FloatField()
	roe = models.FloatField()
	roa = models.FloatField()
	debtratio = models.FloatField()
	err = models.FloatField()
	eps = models.IntegerField()
	per = models.FloatField()
	bps = models.FloatField()
	pbr = models.FloatField()
	dps = models.FloatField()
	rcdp = models.FloatField()
	cdr = models.FloatField()
	stock = models.IntegerField()
