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
		db_table = 'stock2015'
	code = models.CharField(primary_key=True, max_length=7)
	sales = models.FloatField()
	businessprofits = models.FloatField()
	continuing = models.FloatField()
	netincome = models.FloatField()
	netincomeruling = models.FloatField()
	netincomenon = models.FloatField()
	asset = models.FloatField()
	liabilities = models.FloatField()
	totalequities = models.FloatField()
	totalequitiesruling = models.FloatField()
	totalequitiesnon = models.FloatField()
	eqities = models.FloatField()
	cashbusiness = models.FloatField()
	cashinvestment = models.FloatField()
	cashfinance = models.FloatField()
	capex = models.FloatField()
	fcf = models.FloatField()
	ibl = models.FloatField()
	roop = models.FloatField()
	netprofitmargin = models.FloatField()
	roe = models.FloatField()
	roa = models.FloatField()
	debtratio = models.FloatField()
	err = models.FloatField()
	eps = models.FloatField()
	per = models.FloatField()
	bps = models.FloatField()
	pbr = models.FloatField()
	dps = models.FloatField()
	rcdp = models.FloatField()
	cdr = models.FloatField()
	stock = models.FloatField()
